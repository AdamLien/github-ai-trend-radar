import { useEffect, useMemo, useState } from 'react'
import { createRoot } from 'react-dom/client'
import data from './generated/radarData.json'
import './styles.css'

const tagOptions = ['MCP', 'Agent', 'Skills', 'RAG', 'Wiki', 'LLM']
const periodOptions = [
  { value: 1, label: '本日' }, { value: 3, label: '3 日' }, { value: 7, label: '7 日' },
  { value: 30, label: '1 個月' }, { value: 90, label: '3 個月' }, { value: 180, label: '半年' }, { value: 365, label: '1 年' },
]
const sortOptions = {
  momentum: ['區間動能', (a, b) => b.windowDelta - a.windowDelta],
  relative: ['相對成長率', (a, b) => b.windowRelativeGrowth - a.windowRelativeGrowth],
  stars: ['總星數', (a, b) => b.stars - a.stars],
  updated: ['最近更新', (a, b) => (b.pushedAt || '').localeCompare(a.pushedAt || '')],
}
const categories = ['All', 'Deep research', 'Demo/content idea', 'Skill candidate', 'Watch', 'Reference only']
const number = new Intl.NumberFormat('en-US')
const isoDaysAgo = (end, days) => new Date(new Date(`${end}T00:00:00Z`).getTime() - days * 86400000).toISOString().slice(0, 10)

function Sparkline({ series, color = '#246bff' }) {
  const values = series.map((point) => point.stars)
  const max = Math.max(...values, 1); const min = Math.min(...values, max); const range = max - min || 1
  const points = values.map((value, index) => `${index * (100 / Math.max(values.length - 1, 1))},${34 - ((value - min) / range) * 27}`).join(' ')
  return <svg className="sparkline" viewBox="0 0 100 38" role="img" aria-label="選定期間 stars 走勢"><polyline points={points} fill="none" stroke={color} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" /></svg>
}

function TimelineChart({ row, rangeLabel, onClose }) {
  const series = row.windowSeries
  const values = series.map((point) => point.stars)
  const max = Math.max(...values, 1); const min = Math.min(...values, max); const range = max - min || 1
  const x = (index) => 54 + index * (602 / Math.max(series.length - 1, 1))
  const y = (value) => 206 - ((value - min) / range) * 156
  const points = series.map((point, index) => `${x(index)},${y(point.stars)}`).join(' ')
  const labelIndexes = series.length <= 7 ? series.map((_, index) => index) : [0, Math.floor((series.length - 1) / 2), series.length - 1]
  return <section className="timeline-panel"><div className="timeline-heading"><div><span>選中 Repository</span><h2>{row.name}</h2><div className="row-tags">{row.tags.map((tag) => <span key={tag} className={`tag ${tag.toLowerCase()}`}>{tag}</span>)}</div></div><div className="timeline-actions"><a href={row.url} target="_blank" rel="noreferrer">GitHub ↗</a><button className="modal-close" onClick={onClose} aria-label="關閉詳細資料">×</button></div></div><div className="timeline-summary"><div><span>{rangeLabel} star 成長</span><strong>+{number.format(row.windowDelta)}</strong></div><div><span>起點</span><strong>{number.format(series[0]?.stars || 0)}</strong></div><div><span>終點</span><strong>{number.format(series.at(-1)?.stars || 0)}</strong></div><div><span>相對成長</span><strong>{row.windowRelativeGrowth}%</strong></div></div><svg className="timeline-chart" viewBox="0 0 680 270" role="img" aria-label={`${row.name} 的 ${rangeLabel} 星數成長時間軸`}>
    {[0, 1, 2, 3].map((line) => <line key={line} x1="54" x2="656" y1={50 + line * 52} y2={50 + line * 52} stroke="#dce4ef" strokeWidth="1" />)}
    <polyline points={points} fill="none" stroke="#0b9c93" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
    {series.map((point, index) => <circle key={point.date} cx={x(index)} cy={y(point.stars)} r="4.5" fill="#fff" stroke="#0b9c93" strokeWidth="3"><title>{`${point.date}: ${number.format(point.stars)} stars`}</title></circle>)}
    {labelIndexes.map((index) => <text key={series[index].date} x={x(index)} y="244" textAnchor="middle" className="axis-label">{series[index].date.slice(5)}</text>)}
  </svg><p className="timeline-caption">{series[0]?.date} → {series.at(-1)?.date}；GitHub API snapshot total stars。</p></section>
}

function TrendChart({ records, rangeLabel }) {
  const rows = records.slice(0, 3); const all = rows.flatMap((row) => row.windowSeries.map((item) => item.stars))
  const min = Math.min(...all, 0); const max = Math.max(...all, 1); const range = max - min || 1; const colors = ['#246bff', '#0b9c93', '#ed7d2b']
  return <div className="chart-panel"><div className="panel-heading"><h2>{rangeLabel}動能</h2><span>Top 3 by delta</span></div><svg viewBox="0 0 520 244" className="trend-chart" role="img" aria-label="熱門 repo 選定期間 stars 趨勢">
    {[0, 1, 2, 3].map((line) => <line key={line} x1="48" x2="510" y1={28 + line * 52} y2={28 + line * 52} stroke="#dce4ef" strokeWidth="1" />)}
    {rows.map((row, index) => { const points = row.windowSeries.map((item, point) => `${48 + point * (462 / Math.max(row.windowSeries.length - 1, 1))},${184 - ((item.stars - min) / range) * 146}`).join(' '); return <polyline key={row.name} points={points} fill="none" stroke={colors[index]} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" /> })}
  </svg><div className="legend">{rows.map((row, index) => <span key={row.name}><i style={{ background: colors[index] }} />{row.name}</span>)}</div></div>
}

function App() {
  const [search, setSearch] = useState(''); const [category, setCategory] = useState('All'); const [tags, setTags] = useState([]); const [sort, setSort] = useState('momentum')
  const [period, setPeriod] = useState(7); const [customStart, setCustomStart] = useState(data.historyDates.at(-7) || data.historyDates[0]); const [customEnd, setCustomEnd] = useState(data.historyDates.at(-1)); const [selectedName, setSelectedName] = useState(data.records[0].name); const [detailOpen, setDetailOpen] = useState(false)
  const range = useMemo(() => { const end = customEnd || data.historyDates.at(-1); const start = period === 'custom' ? customStart : isoDaysAgo(end, period); return { start, end } }, [period, customStart, customEnd])
  const rangeLabel = period === 'custom' ? '自訂區間' : periodOptions.find((item) => item.value === period)?.label || '7 日'
  const decorated = useMemo(() => data.records.map((row) => { const windowSeries = row.series.filter((point) => point.date >= range.start && point.date <= range.end); const usable = windowSeries.length ? windowSeries : row.series.slice(-1); const windowDelta = Math.max(0, (usable.at(-1)?.stars || 0) - (usable[0]?.stars || 0)); return { ...row, windowSeries: usable, windowDelta, windowRelativeGrowth: Number((windowDelta / Math.max(usable[0]?.stars || 1, 1) * 100).toFixed(3)) } }), [range])
  const filtered = useMemo(() => decorated.filter((row) => { const needle = search.trim().toLowerCase(); const searchable = `${row.name} ${row.description} ${row.tags.join(' ')}`.toLowerCase(); return (!needle || searchable.includes(needle)) && (category === 'All' || row.category === category) && tags.every((tag) => row.tags.includes(tag)) }).sort(sortOptions[sort][1]), [decorated, search, category, tags, sort])
  const selected = decorated.find((row) => row.name === selectedName) || decorated[0]
  const coverageStart = selected.windowSeries[0]?.date || range.start
  const coverageEnd = selected.windowSeries.at(-1)?.date || range.end
  const categoryCounts = categories.slice(1).map((item) => ({ name: item, count: decorated.filter((row) => row.category === item).length })); const maxCount = Math.max(...categoryCounts.map((item) => item.count), 1)
  const toggleTag = (tag) => setTags((current) => current.includes(tag) ? current.filter((item) => item !== tag) : [...current, tag])
  const choosePeriod = (value) => { setPeriod(value); if (value !== 'custom') setCustomEnd(data.historyDates.at(-1)) }
  const openDetail = (name) => { setSelectedName(name); setDetailOpen(true) }
  useEffect(() => { const closeOnEscape = (event) => { if (event.key === 'Escape') setDetailOpen(false) }; window.addEventListener('keydown', closeOnEscape); return () => window.removeEventListener('keydown', closeOnEscape) }, [])
  const availableDays = Math.max(1, Math.round((new Date(`${data.historyDates.at(-1)}T00:00:00Z`) - new Date(`${data.historyDates[0]}T00:00:00Z`)) / 86400000))
  return <main className="app-shell"><aside className="sidebar"><div className="radar-mark"><span /><span /><b>↗</b></div><nav><a className="active" href="#radar">⌁ <span>今日動能</span></a><button className="nav-button" onClick={() => setDetailOpen(true)}>⌁ <span>時間軸</span></button><a href="#categories">◔ <span>分類分佈</span></a><a href="#watchlist">♧ <span>追蹤清單</span></a></nav><p className="source">資料來源：<br />GitHub API snapshots</p></aside>
    <section className="workspace" id="radar"><header><div><h1>GitHub AI Trend Radar</h1><p>AI、MCP、Skills、Agent、LLM、RAG 與 knowledge tools 的每日動能。</p></div><div className="updated">最後更新<br /><strong>{data.updatedAt}</strong></div></header>
      <section className="range-panel" aria-label="日期區間"><div><span className="control-label">日期區間</span><div className="period-buttons">{periodOptions.map((item) => <button key={item.value} className={period === item.value ? 'period active' : 'period'} onClick={() => choosePeriod(item.value)}>{item.label}</button>)}<button className={period === 'custom' ? 'period active' : 'period'} onClick={() => choosePeriod('custom')}>自訂</button></div></div><div className="range-custom"><label>開始<input type="date" min={data.historyDates[0]} max={customEnd} value={customStart} onChange={(event) => { setPeriod('custom'); setCustomStart(event.target.value) }} /></label><span>→</span><label>結束<input type="date" min={customStart} max={data.historyDates.at(-1)} value={customEnd} onChange={(event) => { setPeriod('custom'); setCustomEnd(event.target.value) }} /></label></div><p>目前可用 {availableDays} 天快照；長期快捷鍵會隨每日資料自動延展。</p></section>
      <section className="filters" aria-label="篩選 controls"><label className="search"><span>⌕</span><input value={search} onChange={(event) => setSearch(event.target.value)} placeholder="搜尋 repo、描述或標籤" /></label><label>分類<select value={category} onChange={(event) => setCategory(event.target.value)}>{categories.map((item) => <option key={item} value={item}>{item === 'All' ? '全部分類' : item}</option>)}</select></label><div className="tag-filter"><span>標籤</span>{tagOptions.map((tag) => <button key={tag} className={tags.includes(tag) ? `tag selected ${tag.toLowerCase()}` : `tag ${tag.toLowerCase()}`} onClick={() => toggleTag(tag)}>{tag}</button>)}</div><label>排序<select value={sort} onChange={(event) => setSort(event.target.value)}>{Object.entries(sortOptions).map(([value, [label]]) => <option key={value} value={value}>{label}（降序）</option>)}</select></label></section>
      <section className="dashboard-grid"><section className="table-panel"><div className="panel-heading"><div><h2>{rangeLabel}動能</h2><p>{coverageStart} → {coverageEnd} 的可用跨快照 star delta。</p></div><span className="result-count">{filtered.length} / {data.repoCount} repos</span></div><div className="table-wrap"><table><thead><tr><th>#</th><th>Repository</th><th>用途</th><th>{rangeLabel} 星星增量</th><th>總星數</th><th>期間走勢</th><th>風險 / 品質</th></tr></thead><tbody>{filtered.slice(0, 12).map((row, index) => <tr key={row.name} className={selected.name === row.name ? 'selected' : ''} onClick={() => openDetail(row.name)}><td className="rank">{index + 1}</td><td><strong>{row.name}</strong><div className="row-tags">{row.tags.slice(0, 2).map((tag) => <span key={tag} className={`tag ${tag.toLowerCase()}`}>{tag}</span>)}</div></td><td className="description">{row.description || 'No description available.'}</td><td className="delta">+{number.format(row.windowDelta)}</td><td>{number.format(row.stars)}</td><td><Sparkline series={row.windowSeries} /></td><td><span className={row.category === 'Watch' ? 'risk warning' : 'risk'}>{row.category === 'Watch' ? '需審核' : row.license}</span></td></tr>)}</tbody></table></div></section><section className="right-rail"><TrendChart records={filtered.length ? filtered : decorated} rangeLabel={rangeLabel} /><div className="category-panel" id="categories"><div className="panel-heading"><h2>分類分佈</h2><span>依 repo 數量</span></div>{categoryCounts.map((item) => <div className="distribution" key={item.name}><span>{item.name}</span><div><i style={{ width: `${item.count / maxCount * 100}%` }} /></div><b>{item.count}</b></div>)}</div></section></section>
      {detailOpen && <div className="detail-modal-backdrop" role="presentation" onMouseDown={(event) => { if (event.target === event.currentTarget) setDetailOpen(false) }}><div className="detail-modal" role="dialog" aria-modal="true" aria-label={`${selected.name} 詳細趨勢`}><TimelineChart row={selected} rangeLabel={rangeLabel} onClose={() => setDetailOpen(false)} /></div></div>}<footer>資料來源：GitHub API snapshots。Trending daily 為即時觀察，不納入本頁時序計算。</footer></section></main>
}

createRoot(document.getElementById('root')).render(<App />)
