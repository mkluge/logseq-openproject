# Logseq Plugin for GitLab

This plugin for [logseq](https://logseq.org) allows linking GitLab issues into pages and journals.

# Setup

Install the plugin via the market place. In the plugin settings you have to enter the URL of your GitLab instance and a Personal Access Token with `api` scope.

Optional settings:
- Limit issues to specific project IDs.
- Filter by labels.
- Choose issue state (opened, closed, all).

# Usage

At the moment the following features are supported:
* /gitlab : Link an issue that is assigned to you into the current page
* /gitlab_comment: Link an issue that is assigned to you into the current page and add a comment to the issue in GitLab and Logseq
