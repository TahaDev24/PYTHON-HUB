# Localization and Right-to-Left Support

## Supported languages

- English (en) is the default language and canonical source for product copy.
- Persian (fa) is the second supported language and uses right-to-left direction.

## Translation rules

- Use stable message keys rather than embedding interface copy in components.
- Keep source strings concise and context-aware.
- Do not concatenate translated sentence fragments.
- Keep placeholders named and consistent between locales.
- Add tests whenever a message key or locale is added.
- Fall back to English when a translation is unavailable.

## Layout direction

The interface must set document language and direction together:

- English: lang=en and dir=ltr.
- Persian: lang=fa and dir=rtl.

Prefer CSS logical properties such as margin-inline-start, padding-inline-end, and border-inline-start instead of left/right-specific properties.

Icons that express direction should mirror where appropriate. Brand marks, media controls, and universal symbols should not be mirrored automatically.

## Verification checklist

- [ ] Navigation order is natural in both directions.
- [ ] Inputs, placeholders, and search results align correctly.
- [ ] Mixed Persian and Latin text remains readable.
- [ ] Numbers, code, paths, and command examples remain LTR where appropriate.
- [ ] Menus and popovers remain inside the viewport.
- [ ] Keyboard navigation works in both directions.
- [ ] No text is clipped at mobile widths.
- [ ] Every visible action has a translated accessible name.

## Current implementation

The Python localization catalog provides a small starter set of messages. The web interface includes a language switch and localized category labels. Full application-wide localization will expand as product features are added.
