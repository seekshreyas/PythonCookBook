Notes :: Ch1 ("Text")
======================

## Overall Notes
- Python strings are __Immutable__ sequences of bytes and characters
    - __Immutable__ : no matter what operation you do on the object you produce a __new__ object, rather than mutating the original object.
- __Encoding__ / __Character Sets__ : standard ways in which sequence of characters are represented as sequence of bytes.
- __Codecs__ (coder/decoder): do the conversion between string to binary and vice versa
- Important Encodings:
    - __UTF-8__ : Unicode 8 bit
    - __ISO-8859-1__ : international standard
- Prepending `r` when defining a string keeps it __raw__
- Preprending `u` when defining a string keeps it __unicode__

## Important Modules

| Module Name | Module Uses |
|:------------|:------------|
| `ConfigParser` | handle configuration files |
| `netrc` | parser for application-specific file format |
| `shlex` | typical tokenizer for basic languages |
| `print` | text from data structures |
| `htmllib` & `HTMLParser` | working with text from socket - text is _streamed_ as packets |
| `re` | regular expressions |


## Important Methogs
| Method Name | Description |
|:------------|:------------|
|`.isdigit()` | all characters are digits |
| `.toupper()` | convert to uppercase |
| `<string>.count(<substring>)` | count of instances of substring in string |


## Good Snippets
```
mystr = "my string"
```


### Stride / Step of the slice of a string
```
mystr[:3:-1] # "gnirts"
mystr[1::2] # "ysrn"
```

### Processing a string one character at a time
```
results = map(do_something, mystr)
```