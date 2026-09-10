import test from 'node:test'
import assert from 'node:assert/strict'
import { readRadarState, writeRadarState } from './radarState.js'

const defaults = {
  language: 'zh', search: '', category: 'All', tags: [], scenarios: [], sort: 'momentum',
  period: 7, customStart: '2026-09-03', customEnd: '2026-09-09', selectedName: 'example/default', detailOpen: false,
}

test('restores a shareable selected repository and filters from the URL', () => {
  const state = readRadarState('?repo=example%2Fradar&detail=1&lang=en&q=mcp&tags=MCP,Agent&scenarios=%E9%96%8B%E7%99%BC%E8%88%87%E6%B8%AC%E8%A9%A6&period=custom&start=2026-09-04&end=2026-09-09', defaults)

  assert.equal(state.selectedName, 'example/radar')
  assert.equal(state.detailOpen, true)
  assert.equal(state.language, 'en')
  assert.deepEqual(state.tags, ['MCP', 'Agent'])
  assert.deepEqual(state.scenarios, ['開發與測試'])
  assert.equal(state.customStart, '2026-09-04')
})

test('drops invalid URL parameters and omits defaults from share URLs', () => {
  const state = readRadarState('?lang=unknown&period=999&detail=nope', defaults)

  assert.equal(state.language, 'zh')
  assert.equal(state.period, 7)
  assert.equal(state.detailOpen, false)
  assert.equal(writeRadarState(defaults, defaults), '')
})
