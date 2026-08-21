import { test, expect } from '@playwright/test'

// See here how to get started:
// https://playwright.dev/docs/intro
test('visits the app root url', async ({ page }) => {
  await page.goto('/')
  // The original 'You did it!' test fails since App.vue has been updated to our 3D map.
  // Instead, wait for the map container to load.
  const mapContainer = page.locator('.map-container');
  await expect(mapContainer).toBeVisible();
})
