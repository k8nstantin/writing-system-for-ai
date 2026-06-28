---
name: verify-before-delivery
description: A rule to always test URLs, deployed code, and web pages (checking HTTP status or functionality) before turning them over to the user. Use this skill whenever providing a link to the user or presenting deployed code.
---

# Verify Before Delivery

This skill enforces a mandatory verification protocol before delivering web links, deployed applications, or deployed code to a user.

## Instructions

Whenever you push code that triggers a deployment (like GitHub Pages) or generate a URL for the user to visit:

1. **Do not assume the URL is live immediately.**
2. Use tools (like `curl`) to test the HTTP status code of the URL.
3. If the URL returns a 404 or an error, do not deliver the link yet.
4. Wait or retry until you receive a `200 Success` or another positive indicator that the site/resource is fully deployed and accessible.
5. Only after successful verification should you present the link to the user.
6. **Interact and Test Functionality:** In addition to network headers, always perform physical or logical checks on the compiled script tags, button attachments, and keyboard typing flows to guarantee 100% bug-free interactive performance on the live deployed page before declaring victory.