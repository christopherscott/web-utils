My Python Web Utils
===================

A collection of scripts I've written to make life easier as a web developer. I'm not sure how useful or contrived these are, but for the most part they're solutions to problems I've faced, and/or something I thought might be fun to write. Either way, cheers :)

Ideas (so far):
------

- localCrawl: created to solve the issue of slow, un-cached sandboxes during development. Also could be called prime-cache. Ideally used in a similar situation. Requires base URL, and then analyzes and crawls any local links it finds (either by looking for relative link href values or matching against hostname). Outputs a (colorized) newline-separated list including response codes.

- stylesByType: created to help identify and extract CSS rules (including selectors) by type. For example: find all "background" rules. Files can also be edited in-line to remove said rules and insert into a new stylesheet. Also can provide stats on rules as well.

- styleChecker: CSS syntax checker