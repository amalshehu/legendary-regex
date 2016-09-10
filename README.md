# legendary-regex
Regular expressions are extremely powerful  in extracting information from text.

### Introduction
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

#### Python Regex Quick Reference
````
[abx-z]	One character of: a, b, or the range x-z
[^abx-z]	One character except: a, b, or the range x-z
a|b	a or b
a?	Zero or one a's (greedy)
a??	Zero or one a's (lazy)
a*	Zero or more a's (greedy)
a*?	Zero or more a's (lazy)
a+	One or more a's (greedy)
a+?	One or more a's (lazy)
a{4}	Exactly 4 a's
a{4,8}	Between (inclusive) 4 and 8 a's
a{9,}	9 or more a's
(?=...)	A positive lookahead
(?!...)	A negative lookahead
(?<=...)	A positive lookbehind
(?<!...)	A negative lookbehind
(?:...)	A non-capturing group
(...)	A capturing group
(?P<n>...)	A capturing group named n
^	Beginning of the string
$	End of the string
\d	A digit (same as [0-9])
\D	A non-digit (same as [^0-9])
\w	A word character (same as [_a-zA-Z0-9])
\W	A non-word character (same as [^_a-zA-Z0-9])
\s	A whitespace character
\S	A non-whitespace character
\b	A word boundary
\B	A non-word boundary
\n	A newline
\t	A tab
\cY	The control character with the hex code Y
\xYY	The character with the hex code YY
\uYYYY	The character with the hex code YYYY
.	Any character
\Y	The Y'th captured group
(?P=n)	The captured group named 'n'
(?#...)	A comment
````
