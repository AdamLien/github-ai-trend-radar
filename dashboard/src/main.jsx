import { useEffect, useMemo, useState } from 'react'
import { createRoot } from 'react-dom/client'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import data from './generated/radarData.json'
import './styles.css'

const categoryKeys = ['All', 'Deep research', 'Demo/content idea', 'Skill candidate', 'Watch', 'Reference only']
const categoryText = {
  All: { zh: '全部分類', en: 'All priorities' },
  'Deep research': { zh: '深度研究', en: 'Deep research' },
  'Demo/content idea': { zh: '內容／示範', en: 'Demo / content' },
  'Skill candidate': { zh: 'Skill 候選', en: 'Skill candidate' },
  Watch: { zh: '持續觀察', en: 'Watch' },
  'Reference only': { zh: '僅供參考', en: 'Reference only' },
}
const tagText = {
  AI: { zh: 'AI', en: 'AI' }, MCP: { zh: 'MCP', en: 'MCP' }, Agent: { zh: 'Agent', en: 'Agent' },
  Skills: { zh: 'Skills', en: 'Skills' }, Coding: { zh: '開發', en: 'Coding' }, Automation: { zh: '自動化', en: 'Automation' },
  Research: { zh: '研究', en: 'Research' }, RAG: { zh: 'RAG', en: 'RAG' }, Knowledge: { zh: '知識', en: 'Knowledge' },
  LLM: { zh: 'LLM', en: 'LLM' }, Wiki: { zh: '知識', en: 'Knowledge' },
}
const copy = {
  zh: {
    subtitle: 'AI、MCP、Skills、Agent、LLM、RAG 與 knowledge tools 的每日動能。', updated: '最後更新', language: '語言',
    dateRange: '日期區間', start: '開始', end: '結束', custom: '自訂', available: (days) => `目前可用 ${days} 天快照；長期快捷鍵會隨每日資料自動延展。`,
    search: '搜尋 repo、用途或標籤', category: '分類', tags: '標籤', sort: '排序', priorityHint: '分類＝編輯優先級；每個 repo 僅一種。',
    tagHint: '標籤＝技術主題；可複選篩選，單一 repo 可有多個。', insight: '動能洞察', topMover: '區間領先', fastGrowth: '相對成長最快', activeTopics: '可用主題標籤',
    momentum: (period) => `${period}動能`, topDelta: '依區間增量 Top 3', coverage: (start, end) => `${start} → ${end} 的可用跨快照 star delta。`,
    count: (shown, total) => `${shown} / ${total} repos`, repo: 'Repository', purpose: '用途', delta: (period) => `${period} 星星增量`, stars: '總星數', updatedOn: '最近更新', trend: '期間走勢', risk: '風險／品質', readme: 'README 摘要', readmeLoading: '正在讀取 GitHub README…', readmeError: '目前無法讀取 README，請改用 GitHub 原始頁面。', readmeMore: '顯示更多', readmeLess: '收合',
    categoryDistribution: '分類分佈', byRepos: '依 repo 數量', selected: '選中 Repository', growth: (period) => `${period} star 成長`, beginning: '起點', ending: '終點', relative: '相對成長', close: '關閉詳細資料',
    source: '資料來源：GitHub API snapshots。Trending daily 為即時觀察，不納入本頁時序計算。', review: '需審核', noDescription: '尚無用途說明。', original: '原始 README 摘要', periodLabels: ['本日', '3 日', '7 日', '1 個月', '3 個月', '半年', '1 年'],
    sortLabels: ['區間動能', '相對成長率', '總星數', '最近更新'], timeline: '時間軸', sourceShort: '資料來源：GitHub API snapshots',
  },
  en: {
    subtitle: 'Daily momentum for AI, MCP, Skills, Agents, LLM, RAG, and knowledge tools.', updated: 'Last updated', language: 'Language',
    dateRange: 'Date range', start: 'Start', end: 'End', custom: 'Custom', available: (days) => `${days} days of snapshots are available; long ranges expand as daily data arrives.`,
    search: 'Search repo, purpose, or tags', category: 'Priority', tags: 'Tags', sort: 'Sort', priorityHint: 'Priority = one editorial action level per repository.',
    tagHint: 'Tags = technical topics; filter with multiple tags and a repository may have several.', insight: 'Momentum insights', topMover: 'Leading mover', fastGrowth: 'Fastest relative growth', activeTopics: 'Available topic tags',
    momentum: (period) => `${period} momentum`, topDelta: 'Top 3 by period delta', coverage: (start, end) => `Comparable snapshot delta from ${start} to ${end}.`,
    count: (shown, total) => `${shown} / ${total} repos`, repo: 'Repository', purpose: 'Purpose', delta: (period) => `${period} star delta`, stars: 'Total stars', updatedOn: 'Last updated', trend: 'Period trend', risk: 'Risk / quality', readme: 'README summary', readmeLoading: 'Loading README from GitHub…', readmeError: 'README is unavailable here. Open the GitHub source instead.', readmeMore: 'Show more', readmeLess: 'Show less',
    categoryDistribution: 'Priority distribution', byRepos: 'Repositories', selected: 'Selected repository', growth: (period) => `${period} star growth`, beginning: 'Start', ending: 'End', relative: 'Relative growth', close: 'Close details',
    source: 'Source: GitHub API snapshots. Trending daily is observed live and excluded from time-series calculations.', review: 'Review needed', noDescription: 'No purpose description available.', original: 'Original README summary', periodLabels: ['Today', '3 days', '7 days', '1 month', '3 months', '6 months', '1 year'],
    sortLabels: ['Period momentum', 'Relative growth', 'Total stars', 'Recently updated'], timeline: 'Timeline', sourceShort: 'Source: GitHub API snapshots',
  },
}
const number = (language) => new Intl.NumberFormat(language === 'zh' ? 'en-US' : 'en-US')
const isoDaysAgo = (end, days) => new Date(new Date(`${end}T00:00:00Z`).getTime() - days * 86400000).toISOString().slice(0, 10)
const readmePlugins = [remarkGfm]
const formatReadme = (raw) => {
  const withoutMedia = raw
    .replace(/\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)/g, '')
    .replace(/<img\b[^>]*>/gi, '')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
  const withoutMarkup = withoutMedia
    .replace(/<[^>]*>/g, '')
    .replace(/\r\n/g, '\n')
  const firstHeading = withoutMarkup.search(/^#{1,2}\s+\S/m)
  return (firstHeading >= 0 ? withoutMarkup.slice(firstHeading) : withoutMarkup)
    .replace(/\n{3,}/g, '\n\n')
    .trim()
    .slice(0, 2800)
}

function Tag({ tag, selected, onClick, language }) {
  const label = tagText[tag]?.[language] || tag
  return <button className={`tag ${selected ? 'selected ' : ''}${tag.toLowerCase()}`} onClick={onClick}>{label}</button>
}

function Sparkline({ series }) {
  const values = series.map((point) => point.stars); const max = Math.max(...values, 1); const min = Math.min(...values, max); const range = max - min || 1
  const points = values.map((value, index) => `${index * (100 / Math.max(values.length - 1, 1))},${34 - ((value - min) / range) * 27}`).join(' ')
  return <svg className="sparkline" viewBox="0 0 100 38" role="img" aria-label="Star trend"><polyline points={points} fill="none" stroke="#246bff" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" /></svg>
}

function TimelineChart({ row, rangeLabel, onClose, language, readme }) {
  const t = copy[language]; const format = number(language); const series = row.windowSeries; const values = series.map((point) => point.stars); const max = Math.max(...values, 1); const min = Math.min(...values, max); const range = max - min || 1
  const x = (index) => 54 + index * (602 / Math.max(series.length - 1, 1)); const y = (value) => 206 - ((value - min) / range) * 156
  const points = series.map((point, index) => `${x(index)},${y(point.stars)}`).join(' '); const labels = series.length <= 7 ? series.map((_, index) => index) : [0, Math.floor((series.length - 1) / 2), series.length - 1]
  return <section className="timeline-panel"><div className="timeline-heading"><div><span>{t.selected}</span><h2>{row.name}</h2><div className="row-tags">{row.tags.map((tag) => <span key={tag} className={`tag ${tag.toLowerCase()}`}>{tagText[tag]?.[language] || tag}</span>)}</div></div><div className="timeline-actions"><a href={row.url} target="_blank" rel="noreferrer">GitHub ↗</a><button className="modal-close" onClick={onClose} aria-label={t.close}>×</button></div></div><p className="purpose-in-modal"><b>{t.purpose}</b>{language === 'zh' ? row.descriptionZh : row.description}</p><div className="timeline-summary"><div><span>{t.growth(rangeLabel)}</span><strong>+{format.format(row.windowDelta)}</strong></div><div><span>{t.beginning}</span><strong>{format.format(series[0]?.stars || 0)}</strong></div><div><span>{t.ending}</span><strong>{format.format(series.at(-1)?.stars || 0)}</strong></div><div><span>{t.relative}</span><strong>{row.windowRelativeGrowth}%</strong></div><div><span>{t.updatedOn}</span><strong>{row.pushedAt || '—'}</strong></div></div><section className="readme-panel"><div><h3>{t.readme}</h3><span>{t.updatedOn}: {row.pushedAt || '—'}</span></div>{readme?.status === 'loading' && <p>{t.readmeLoading}</p>}{readme?.status === 'error' && <p>{t.readmeError}</p>}{readme?.content && <details><summary>{t.readmeMore}</summary><div className="readme-markdown"><ReactMarkdown remarkPlugins={readmePlugins}>{readme.content}</ReactMarkdown></div></details>}</section><svg className="timeline-chart" viewBox="0 0 680 270" role="img" aria-label={`${row.name} star trend`}>
    {[0, 1, 2, 3].map((line) => <line key={line} x1="54" x2="656" y1={50 + line * 52} y2={50 + line * 52} stroke="#dce4ef" strokeWidth="1" />)}<polyline points={points} fill="none" stroke="#0b9c93" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
    {series.map((point, index) => <circle key={point.date} cx={x(index)} cy={y(point.stars)} r="4.5" fill="#fff" stroke="#0b9c93" strokeWidth="3"><title>{`${point.date}: ${format.format(point.stars)} stars`}</title></circle>)}{labels.map((index) => <text key={series[index].date} x={x(index)} y="244" textAnchor="middle" className="axis-label">{series[index].date.slice(5)}</text>)}</svg><p className="timeline-caption">{series[0]?.date} → {series.at(-1)?.date} · GitHub API snapshot total stars.</p></section>
}

function TrendChart({ records, rangeLabel, language }) {
  const t = copy[language]; const rows = records.slice(0, 3); const all = rows.flatMap((row) => row.windowSeries.map((item) => item.stars)); const min = Math.min(...all, 0); const max = Math.max(...all, 1); const range = max - min || 1; const colors = ['#246bff', '#0b9c93', '#ed7d2b']
  return <div className="chart-panel"><div className="panel-heading"><h2>{t.momentum(rangeLabel)}</h2><span>{t.topDelta}</span></div><svg viewBox="0 0 520 244" className="trend-chart" role="img" aria-label="Top repository trends">{[0, 1, 2, 3].map((line) => <line key={line} x1="48" x2="510" y1={28 + line * 52} y2={28 + line * 52} stroke="#dce4ef" strokeWidth="1" />)}{rows.map((row, index) => { const points = row.windowSeries.map((item, point) => `${48 + point * (462 / Math.max(row.windowSeries.length - 1, 1))},${184 - ((item.stars - min) / range) * 146}`).join(' '); return <polyline key={row.name} points={points} fill="none" stroke={colors[index]} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" /> })}</svg><div className="legend">{rows.map((row, index) => <span key={row.name}><i style={{ background: colors[index] }} />{row.name}</span>)}</div></div>
}

function InsightPanel({ records, tagOptions, language }) {
  const t = copy[language]; const fastest = [...records].sort((a, b) => b.windowRelativeGrowth - a.windowRelativeGrowth)[0]; const leader = records[0]
  return <section className="insight-panel"><div className="panel-heading"><h2>{t.insight}</h2><span>{t.momentum('')}</span></div><div className="insight-list"><div><span>{t.topMover}</span><strong>{leader?.name || '—'}</strong></div><div><span>{t.fastGrowth}</span><strong>{fastest?.name || '—'}</strong></div><div><span>{t.activeTopics}</span><strong>{tagOptions.length}</strong></div></div></section>
}

function App() {
  const [language, setLanguage] = useState('zh'); const [search, setSearch] = useState(''); const [category, setCategory] = useState('All'); const [tags, setTags] = useState([]); const [sort, setSort] = useState('momentum'); const [period, setPeriod] = useState(7)
  const [customStart, setCustomStart] = useState(data.historyDates.at(-7) || data.historyDates[0]); const [customEnd, setCustomEnd] = useState(data.historyDates.at(-1)); const [selectedName, setSelectedName] = useState(data.records[0].name); const [detailOpen, setDetailOpen] = useState(false); const [readmes, setReadmes] = useState({})
  const t = copy[language]; const tagOptions = useMemo(() => [...new Set(data.records.flatMap((row) => row.tags))].sort(), []); const periodOptions = t.periodLabels.map((label, index) => ({ value: [1, 3, 7, 30, 90, 180, 365][index], label }))
  const sortOptions = { momentum: [t.sortLabels[0], (a, b) => b.windowDelta - a.windowDelta], relative: [t.sortLabels[1], (a, b) => b.windowRelativeGrowth - a.windowRelativeGrowth], stars: [t.sortLabels[2], (a, b) => b.stars - a.stars], updated: [t.sortLabels[3], (a, b) => (b.pushedAt || '').localeCompare(a.pushedAt || '')] }
  const range = useMemo(() => { const end = customEnd || data.historyDates.at(-1); return { start: period === 'custom' ? customStart : isoDaysAgo(end, period), end } }, [period, customStart, customEnd]); const rangeLabel = period === 'custom' ? t.custom : periodOptions.find((item) => item.value === period)?.label || t.periodLabels[2]
  const decorated = useMemo(() => data.records.map((row) => { const points = row.series.filter((point) => point.date >= range.start && point.date <= range.end); const windowSeries = points.length ? points : row.series.slice(-1); const windowDelta = Math.max(0, (windowSeries.at(-1)?.stars || 0) - (windowSeries[0]?.stars || 0)); return { ...row, windowSeries, windowDelta, windowRelativeGrowth: Number((windowDelta / Math.max(windowSeries[0]?.stars || 1, 1) * 100).toFixed(3)) } }), [range])
  const filtered = useMemo(() => decorated.filter((row) => { const needle = search.trim().toLowerCase(); const searchable = `${row.name} ${row.description} ${row.descriptionZh} ${row.tags.join(' ')}`.toLowerCase(); return (!needle || searchable.includes(needle)) && (category === 'All' || row.category === category) && tags.every((tag) => row.tags.includes(tag)) }).sort(sortOptions[sort][1]), [decorated, search, category, tags, sort])
  const selected = decorated.find((row) => row.name === selectedName) || decorated[0]; const coverageStart = selected.windowSeries[0]?.date || range.start; const coverageEnd = selected.windowSeries.at(-1)?.date || range.end; const categoryCounts = categoryKeys.slice(1).map((key) => ({ key, count: decorated.filter((row) => row.category === key).length })); const maxCount = Math.max(...categoryCounts.map((item) => item.count), 1); const days = Math.max(1, Math.round((new Date(`${data.historyDates.at(-1)}T00:00:00Z`) - new Date(`${data.historyDates[0]}T00:00:00Z`)) / 86400000))
  const loadReadme = async (row) => { if (readmes[row.name]) return; setReadmes((current) => ({ ...current, [row.name]: { status: 'loading' } })); try { const response = await fetch(`https://api.github.com/repos/${row.name}/readme`, { headers: { Accept: 'application/vnd.github.raw+json' } }); if (!response.ok) throw new Error(`GitHub ${response.status}`); const content = formatReadme(await response.text()); setReadmes((current) => ({ ...current, [row.name]: { status: 'ready', content } })); } catch { setReadmes((current) => ({ ...current, [row.name]: { status: 'error' } })); } }
  const toggleTag = (tag) => setTags((current) => current.includes(tag) ? current.filter((item) => item !== tag) : [...current, tag]); const choosePeriod = (value) => { setPeriod(value); if (value !== 'custom') setCustomEnd(data.historyDates.at(-1)) }; const openDetail = (name) => { const row = decorated.find((item) => item.name === name); setSelectedName(name); setDetailOpen(true); if (row) loadReadme(row) }
  useEffect(() => { const closeOnEscape = (event) => { if (event.key === 'Escape') setDetailOpen(false) }; window.addEventListener('keydown', closeOnEscape); return () => window.removeEventListener('keydown', closeOnEscape) }, []); useEffect(() => { document.documentElement.lang = language === 'zh' ? 'zh-Hant' : 'en' }, [language])
  return <main className="app-shell"><aside className="sidebar"><div className="radar-mark" aria-label="GitHub AI Trend Radar"><span /><span /><b>↗</b></div><div className="side-status"><strong>Radar</strong><span>{data.updatedAt}</span></div><p className="source">{t.sourceShort}</p></aside><section className="workspace" id="radar"><header><div><h1>GitHub AI Trend Radar</h1><p>{t.subtitle}</p></div><div className="header-tools"><div className="language-switch" aria-label={t.language}><button className={language === 'zh' ? 'active' : ''} onClick={() => setLanguage('zh')}>繁中</button><button className={language === 'en' ? 'active' : ''} onClick={() => setLanguage('en')}>EN</button></div><div className="updated">{t.updated}<strong>{data.updatedAt}</strong></div></div></header>
    <section className="range-panel" aria-label={t.dateRange}><div><span className="control-label">{t.dateRange}</span><div className="period-buttons">{periodOptions.map((item) => <button key={item.value} className={period === item.value ? 'period active' : 'period'} onClick={() => choosePeriod(item.value)}>{item.label}</button>)}<button className={period === 'custom' ? 'period active' : 'period'} onClick={() => choosePeriod('custom')}>{t.custom}</button></div></div><div className="range-custom"><label>{t.start}<input type="date" min={data.historyDates[0]} max={customEnd} value={customStart} onChange={(event) => { setPeriod('custom'); setCustomStart(event.target.value) }} /></label><span>→</span><label>{t.end}<input type="date" min={customStart} max={data.historyDates.at(-1)} value={customEnd} onChange={(event) => { setPeriod('custom'); setCustomEnd(event.target.value) }} /></label></div><p>{t.available(days)}</p></section>
    <section className="filters" aria-label="Filter controls"><label className="search"><span>⌕</span><input value={search} onChange={(event) => setSearch(event.target.value)} placeholder={t.search} /></label><label>{t.category}<select value={category} onChange={(event) => setCategory(event.target.value)}>{categoryKeys.map((key) => <option key={key} value={key}>{categoryText[key][language]}</option>)}</select></label><div className="tag-filter"><span>{t.tags}</span>{tagOptions.map((tag) => <Tag key={tag} tag={tag} selected={tags.includes(tag)} onClick={() => toggleTag(tag)} language={language} />)}</div><label>{t.sort}<select value={sort} onChange={(event) => setSort(event.target.value)}>{Object.entries(sortOptions).map(([value, [label]]) => <option key={value} value={value}>{label}</option>)}</select></label><div className="filter-notes"><span><b>{t.category}</b>{t.priorityHint}</span><span><b>{t.tags}</b>{t.tagHint}</span></div></section>
    <section className="dashboard-grid"><section className="table-panel"><div className="panel-heading"><div><h2>{t.momentum(rangeLabel)}</h2><p>{t.coverage(coverageStart, coverageEnd)}</p></div><span className="result-count">{t.count(filtered.length, data.repoCount)}</span></div><div className="table-wrap"><table><thead><tr><th>#</th><th>{t.repo}</th><th>{t.purpose}</th><th>{t.delta(rangeLabel)}</th><th>{t.stars}</th><th>{t.updatedOn}</th><th>{t.trend}</th><th>{t.risk}</th></tr></thead><tbody>{filtered.slice(0, 12).map((row, index) => <tr key={row.name} className={selected.name === row.name ? 'selected' : ''} onClick={() => openDetail(row.name)}><td className="rank">{index + 1}</td><td><strong>{row.name}</strong><div className="row-tags">{row.tags.slice(0, 3).map((tag) => <span key={tag} className={`tag ${tag.toLowerCase()}`}>{tagText[tag]?.[language] || tag}</span>)}</div></td><td className="description"><span>{language === 'zh' ? row.descriptionZh : row.description || t.noDescription}</span>{language === 'zh' && <small>{t.original}</small>}</td><td className="delta">+{number(language).format(row.windowDelta)}</td><td>{number(language).format(row.stars)}</td><td className="updated-date">{row.pushedAt || '—'}</td><td><Sparkline series={row.windowSeries} /></td><td><span className={row.category === 'Watch' ? 'risk warning' : 'risk'}>{row.category === 'Watch' ? t.review : row.license}</span></td></tr>)}</tbody></table></div></section><section className="right-rail"><InsightPanel records={filtered.length ? filtered : decorated} tagOptions={tagOptions} language={language} /><TrendChart records={filtered.length ? filtered : decorated} rangeLabel={rangeLabel} language={language} /><div className="category-panel"><div className="panel-heading"><h2>{t.categoryDistribution}</h2><span>{t.byRepos}</span></div>{categoryCounts.map((item) => <div className="distribution" key={item.key}><span>{categoryText[item.key][language]}</span><div><i style={{ width: `${item.count / maxCount * 100}%` }} /></div><b>{item.count}</b></div>)}</div></section></section>
    {detailOpen && <div className="detail-modal-backdrop" role="presentation" onMouseDown={(event) => { if (event.target === event.currentTarget) setDetailOpen(false) }}><div className="detail-modal" role="dialog" aria-modal="true" aria-label={`${selected.name} ${t.timeline}`}><TimelineChart row={selected} rangeLabel={rangeLabel} onClose={() => setDetailOpen(false)} language={language} readme={readmes[selected.name]} /></div></div>}<footer>{t.source}</footer></section></main>
}

createRoot(document.getElementById('root')).render(<App />)
