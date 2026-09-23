import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import test from 'node:test'

test('renders weekly notes in the right rail after momentum insights', () => {
  const source = readFileSync(new URL('./main.jsx', import.meta.url), 'utf8')
  const grid = source.indexOf('<section className="dashboard-grid">')
  const rightRail = source.indexOf('<section className="right-rail">', grid)
  const insight = source.indexOf('<InsightPanel records=', rightRail)
  const weekly = source.lastIndexOf('<WeeklyNotes notes=')

  assert.ok(grid >= 0)
  assert.ok(rightRail > grid)
  assert.ok(insight > rightRail)
  assert.ok(weekly > insight, 'weekly notes should not interrupt the filters-to-table flow')
})
