const PERIODS = new Set([1, 3, 7, 30, 90, 180, 365])
const LANGUAGES = new Set(['zh', 'en'])

const dateOr = (value, fallback) => /^\d{4}-\d{2}-\d{2}$/.test(value || '') ? value : fallback
const values = (value) => value ? value.split(',').filter(Boolean) : []

export function readRadarState(search, defaults) {
  const params = new URLSearchParams(search)
  const language = params.get('lang')
  const requestedPeriod = params.get('period')
  const numericPeriod = Number(requestedPeriod)
  const period = requestedPeriod === 'custom' || PERIODS.has(numericPeriod) ? (requestedPeriod === 'custom' ? 'custom' : numericPeriod) : defaults.period
  const selectedName = params.get('repo') || defaults.selectedName
  return {
    ...defaults,
    language: LANGUAGES.has(language) ? language : defaults.language,
    search: params.get('q') || defaults.search,
    category: params.get('category') || defaults.category,
    tags: values(params.get('tags')),
    scenarios: values(params.get('scenarios')),
    sort: params.get('sort') || defaults.sort,
    period,
    customStart: dateOr(params.get('start'), defaults.customStart),
    customEnd: dateOr(params.get('end'), defaults.customEnd),
    selectedName,
    detailOpen: params.get('detail') === '1' && Boolean(params.get('repo')),
  }
}

export function writeRadarState(state, defaults) {
  const params = new URLSearchParams()
  const set = (key, value, defaultValue) => {
    if (value !== defaultValue && value !== '' && value != null) params.set(key, String(value))
  }
  set('lang', state.language, defaults.language)
  set('q', state.search, defaults.search)
  set('category', state.category, defaults.category)
  set('sort', state.sort, defaults.sort)
  if (state.tags.length) params.set('tags', state.tags.join(','))
  if (state.scenarios.length) params.set('scenarios', state.scenarios.join(','))
  if (state.period !== defaults.period) params.set('period', state.period)
  if (state.period === 'custom') {
    set('start', state.customStart, defaults.customStart)
    set('end', state.customEnd, defaults.customEnd)
  }
  if (state.detailOpen && state.selectedName) {
    params.set('repo', state.selectedName)
    params.set('detail', '1')
  }
  return params.toString()
}
