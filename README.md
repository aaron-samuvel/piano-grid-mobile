# Piano Grid Mobile

An Expo / React Native starter for the Piano Grid daily piano trainer.

## Start

1. Install Node.js and the Expo prerequisites for your target device.
2. Run `npm install` in this folder.
3. Run `npm run android` or `npm start` and launch the app with Expo Go or a development build.

## Included vertical slice

- First-run welcome and five-tab mobile navigation.
- A daily note-finding exercise on a playable one-octave keyboard.
- Locally bundled chromatic practice tones (simple synthesized tones, not piano recordings).
- On-device progress persistence, attempt history, streak, and guarded daily XP rewards.
- Workbook page groups based on visual inspection of the 72-page scan.
- Clearly labeled demo coach; no AI credentials or server integration are configured.

## Workbook source

The source workbook is a scanned PDF with no searchable text layer. The lesson page groups reference pages 1-4, 5-24, 25-48, and 49-72 as broad practice segments, not as printed chapter boundaries. The PDF itself is not copied into this app. Each source action instructs the learner to open the original file and navigate to those pages.

## Current limits

Progress is local to this device. There is no authentication, account sync, cloud AI tutor, notification scheduling, offline sync queue, or embedded PDF viewer yet. The visual piano currently covers one octave and note-name matching; it does not render staff notation or recognize acoustic piano input. Test sound latency and touch behavior on physical Android and iOS devices before release.

## Publish the mobile app separately

The mobile app is intended for a separate public repository named `piano-grid-mobile`; do not put it in the website repository. Its GitHub Actions workflow builds an Android APK with Expo Application Services (EAS) and attaches the APK to a GitHub Release.

One-time setup:

1. Create/link the Expo project from this directory with `npx eas-cli login` and `npx eas-cli init`.
2. Add the generated `extra.eas.projectId` in `app.json` to Git, but never commit credentials or signing keys.
3. Create an Expo access token and add it to the mobile GitHub repository as an Actions secret named `EXPO_TOKEN`.
4. Push the `main` branch or run **Actions → Build Android APK → Run workflow**. Each successful run creates a GitHub Release with the APK attached.

EAS supplies the Android signing credentials for this preview build. The GitHub workflow does not upload any signing keystore. For a local build alternative, follow the EAS commands above and download the artifact from the EAS build page.
