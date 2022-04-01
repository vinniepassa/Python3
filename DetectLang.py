import time
import string
import os
from scipy import spatial

#baseDict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
baseChars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","â","á","å","ä","ã","ą","æ","œ","ç","ĉ","ć","č","ď","ð","è","é","ê","ë","ę","ě","ĝ","ğ","ĥ","î","ì","í","ï","ı","ĵ","ł","ñ","ń",	"ň",	"ò",	"ö",	"ô",	"ó",	"õ",	"ø",	"ř",	"ŝ",	"ş",	"ś",	"š",	"ß",	"ť",	"þ",	"ù",	"ú",	"û",	"ŭ",	"ü",	"ů",	"ý",	"ź",	"ż",	"ž"]

dictEN = {"a":8.167,	"b":1.492,	"c":2.782,	"d":4.253,	"e":12.702,	"f":2.228,	"g":2.015,	"h":6.094,	"i":6.966,	"j":0.153,	"k":0.772,	"l":4.025,	"m":2.406,	"n":6.749,	"o":7.507,	"p":1.929,	"q":0.095,	"r":5.987,	"s":6.327,	"t":9.056,	"u":2.758,	"v":0.978,	"w":2.36,	"x":0.15,	"y":1.974,	"z":0.074,	"à":0,	"â":0,	"á":0,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0,	"ô":0,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictFR = {"a":7.636,	"b":0.901,	"c":3.26,	"d":3.669,	"e":14.715,	"f":1.066,	"g":0.866,	"h":0.737,	"i":7.529,	"j":0.613,	"k":0.049,	"l":5.456,	"m":2.968,	"n":7.095,	"o":5.796,	"p":2.521,	"q":1.362,	"r":6.693,	"s":7.948,	"t":7.244,	"u":6.311,	"v":1.838,	"w":0.074,	"x":0.427,	"y":0.128,	"z":0.326,	"à":0.486,	"â":0.051,	"á":0,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0,	"œ":0.018,	"ç":0.085,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0.271,	"é":1.504,	"ê":0.218,	"ë":0.008,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0.045,	"ì":0,	"í":0,	"ï":0.005,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0,	"ô":0.023,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0.058,	"ú":0,	"û":0.06,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictDE = {"a":6.516,	"b":1.886,	"c":2.732,	"d":5.076,	"e":16.396,	"f":1.656,	"g":3.009,	"h":4.577,	"i":6.55,	"j":0.268,	"k":1.417,	"l":3.437,	"m":2.534,	"n":9.776,	"o":2.594,	"p":0.67,	"q":0.018,	"r":7.003,	"s":7.27,	"t":6.154,	"u":4.166,	"v":0.846,	"w":1.921,	"x":0.034,	"y":0.039,	"z":1.134,	"à":0,	"â":0,	"á":0,	"å":0,	"ä":0.578,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0.443,	"ô":0,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0.307,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":0.995,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictES = {"a":11.525,	"b":2.215,	"c":4.019,	"d":5.01,	"e":12.181,	"f":0.692,	"g":1.768,	"h":0.703,	"i":6.247,	"j":0.493,	"k":0.011,	"l":4.967,	"m":3.157,	"n":6.712,	"o":8.683,	"p":2.51,	"q":0.877,	"r":6.871,	"s":7.977,	"t":4.632,	"u":2.927,	"v":1.138,	"w":0.017,	"x":0.215,	"y":1.008,	"z":0.467,	"à":0,	"â":0,	"á":0.502,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0.433,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0.725,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0.311,	"ń":0,	"ň":0,	"ò":0,	"ö":0,	"ô":0,	"ó":0.827,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0.168,	"û":0,	"ŭ":0,	"ü":0.012,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictPT = {"a":14.634,	"b":1.043,	"c":3.882,	"d":4.992,	"e":12.57,	"f":1.023,	"g":1.303,	"h":0.781,	"i":6.186,	"j":0.397,	"k":0.015,	"l":2.779,	"m":4.738,	"n":4.446,	"o":9.735,	"p":2.523,	"q":1.204,	"r":6.53,	"s":6.805,	"t":4.336,	"u":3.639,	"v":1.575,	"w":0.037,	"x":0.253,	"y":0.006,	"z":0.47,	"à":0.072,	"â":0.562,	"á":0.118,	"å":0,	"ä":0,	"ã":0.733,	"ą":0,	"æ":0,	"œ":0,	"ç":0.53,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0.337,	"ê":0.45,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0.132,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0,	"ô":0.635,	"ó":0.296,	"õ":0.04,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0.207,	"û":0,	"ŭ":0,	"ü":0.026,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictIT = {"a":11.745,	"b":0.927,	"c":4.501,	"d":3.736,	"e":11.792,	"f":1.163,	"g":1.644,	"h":0.636,	"i":10.143,	"j":0.011,	"k":0.009,	"l":6.51,	"m":2.512,	"n":6.883,	"o":9.832,	"p":3.056,	"q":0.505,	"r":6.367,	"s":4.981,	"t":5.623,	"u":3.011,	"v":2.097,	"w":0.033,	"x":0.003,	"y":0.02,	"z":1.181,	"à":0.635,	"â":0,	"á":0,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0.263,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0.03,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0.002,	"ö":0,	"ô":0,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0.166,	"ú":0,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictTK = {"a":12.92,	"b":2.844,	"c":1.463,	"d":5.206,	"e":9.912,	"f":0.461,	"g":1.253,	"h":1.212,	"i":9.6,	"j":0.034,	"k":5.683,	"l":5.922,	"m":3.752,	"n":7.987,	"o":2.976,	"p":0.886,	"q":0,	"r":7.722,	"s":3.014,	"t":3.314,	"u":3.235,	"v":0.959,	"w":0,	"x":0,	"y":3.336,	"z":1.5,	"à":0,	"â":0,	"á":0,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":1.156,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":1.125,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":5.114,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0.777,	"ô":0,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":1.78,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":1.854,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictSW = {"a":9.383,	"b":1.535,	"c":1.486,	"d":4.702,	"e":10.149,	"f":2.027,	"g":2.862,	"h":2.09,	"i":5.817,	"j":0.614,	"k":3.14,	"l":5.275,	"m":3.471,	"n":8.542,	"o":4.482,	"p":1.839,	"q":0.02,	"r":8.431,	"s":6.59,	"t":7.691,	"u":1.919,	"v":2.415,	"w":0.142,	"x":0.159,	"y":0.708,	"z":0.07,	"à":0,	"â":0,	"á":0,	"å":1.338,	"ä":1.797,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":1.305,	"ô":0,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictPL = {"a":10.503,	"b":1.74,	"c":3.895,	"d":3.725,	"e":7.352,	"f":0.143,	"g":1.731,	"h":1.015,	"i":8.328,	"j":1.836,	"k":2.753,	"l":2.564,	"m":2.515,	"n":6.237,	"o":6.667,	"p":2.445,	"q":0,	"r":5.243,	"s":5.224,	"t":2.475,	"u":2.062,	"v":0.012,	"w":5.813,	"x":0.004,	"y":3.206,	"z":4.852,	"à":0,	"â":0,	"á":0,	"å":0,	"ä":0,	"ã":0,	"ą":0.699,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0.743,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":1.035,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":2.109,	"ñ":0,	"ń":0.362,	"ň":0,	"ò":0,	"ö":0,	"ô":0,	"ó":1.141,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0.814,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0.078,	"ż":0.706,	"ž":0}
dictNL = {"a":7.486,	"b":1.584,	"c":1.242,	"d":5.933,	"e":18.91,	"f":0.805,	"g":3.403,	"h":2.38,	"i":6.499,	"j":1.46,	"k":2.248,	"l":3.568,	"m":2.213,	"n":10.032,	"o":6.063,	"p":1.57,	"q":0.009,	"r":6.411,	"s":3.73,	"t":6.79,	"u":1.99,	"v":2.85,	"w":1.52,	"x":0.036,	"y":0.035,	"z":1.39,	"à":0,	"â":0,	"á":0,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0,	"ô":0,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictDK = {"a":6.025,	"b":2,	"c":0.565,	"d":5.858,	"e":15.453,	"f":2.406,	"g":4.077,	"h":1.621,	"i":6,	"j":0.73,	"k":3.395,	"l":5.229,	"m":3.237,	"n":7.24,	"o":4.636,	"p":1.756,	"q":0.007,	"r":8.956,	"s":5.805,	"t":6.862,	"u":1.979,	"v":2.332,	"w":0.069,	"x":0.028,	"y":0.698,	"z":0.034,	"à":0,	"â":0,	"á":0,	"å":1.19,	"ä":0,	"ã":0,	"ą":0,	"æ":0.872,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0,	"ô":0,	"ó":0,	"õ":0,	"ø":0.939,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictIS = {"a":10.11,	"b":1.043,	"c":0,	"d":1.575,	"e":6.418,	"f":3.013,	"g":4.241,	"h":1.871,	"i":7.578,	"j":1.144,	"k":3.314,	"l":4.532,	"m":4.041,	"n":7.711,	"o":2.166,	"p":0.789,	"q":0,	"r":8.581,	"s":5.63,	"t":4.953,	"u":4.562,	"v":2.437,	"w":0,	"x":0.046,	"y":0.9,	"z":0,	"à":0,	"â":0,	"á":1.799,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0.867,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":4.393,	"è":0,	"é":0.647,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":1.57,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0.777,	"ô":0,	"ó":0.994,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":1.455,	"ù":0,	"ú":0.613,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0.228,	"ź":0,	"ż":0,	"ž":0}
dictFI = {"a":12.217,	"b":0.281,	"c":0.281,	"d":1.043,	"e":7.968,	"f":0.194,	"g":0.392,	"h":1.851,	"i":10.817,	"j":2.042,	"k":4.973,	"l":5.761,	"m":3.202,	"n":8.826,	"o":5.614,	"p":1.842,	"q":0.013,	"r":2.872,	"s":7.862,	"t":8.75,	"u":5.008,	"v":2.25,	"w":0.094,	"x":0.031,	"y":1.745,	"z":0.051,	"à":0,	"â":0,	"á":0,	"å":0.003,	"ä":3.577,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0,	"ď":0,	"ð":0,	"è":0,	"é":0,	"ê":0,	"ë":0,	"ę":0,	"ě":0,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":0,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0,	"ò":0,	"ö":0.444,	"ô":0,	"ó":0,	"õ":0,	"ø":0,	"ř":0,	"ŝ":0,	"ş":0,	"ś":0,	"š":0,	"ß":0,	"ť":0,	"þ":0,	"ù":0,	"ú":0,	"û":0,	"ŭ":0,	"ü":0,	"ů":0,	"ý":0,	"ź":0,	"ż":0,	"ž":0}
dictCZ = {"a":8.421,	"b":0.822,	"c":0.74,	"d":3.475,	"e":7.562,	"f":0.084,	"g":0.092,	"h":1.356,	"i":6.073,	"j":1.433,	"k":2.894,	"l":3.802,	"m":2.446,	"n":6.468,	"o":6.695,	"p":1.906,	"q":0.001,	"r":4.799,	"s":5.212,	"t":5.727,	"u":2.16,	"v":5.344,	"w":0.016,	"x":0.027,	"y":1.043,	"z":1.503,	"à":0,	"â":0,	"á":0.867,	"å":0,	"ä":0,	"ã":0,	"ą":0,	"æ":0,	"œ":0,	"ç":0,	"ĉ":0,	"ć":0,	"č":0.462,	"ď":0.015,	"ð":0,	"è":0,	"é":0.633,	"ê":0,	"ë":0,	"ę":0,	"ě":1.222,	"ĝ":0,	"ğ":0,	"ĥ":0,	"î":0,	"ì":0,	"í":1.643,	"ï":0,	"ı":0,	"ĵ":0,	"ł":0,	"ñ":0,	"ń":0,	"ň":0.007,	"ò":0,	"ö":0,	"ô":0,	"ó":0.024,	"õ":0,	"ø":0,	"ř":0.38,	"ŝ":0,	"ş":0,	"ś":0,	"š":0.688,	"ß":0,	"ť":0.006,	"þ":0,	"ù":0,	"ú":0.045,	"û":0,	"ŭ":0,	"ü":0,	"ů":0.204,	"ý":0.995,	"ź":0,	"ż":0,	"ž":0.721}
dictNO = {"a":6.07, "b":1.47, "c":0.34, "d":4.21, "e":15.38, "f":2.02, "g":3.9, "h":1.64, "i":6.16, "j":1.02, "k":3.83, "l":5.26, "m":3.4, "n":7.81, "o":5.03, "p":2.06, "q":0.02, "r":8.53, "s":6.36, "t":7.84, "u":1.8, "v":2.4, "w":0.15, "x":0.05, "y":0.74, "z":0.04, "à":0, "â":0, "á":0, "å":1.5, "ä":0, "ã":0, "ą":0, "æ":0.2, "œ":0, "ç":0, "ĉ":0, "ć":0, "č":0, "ď":0, "ð":0, "è":0, "é":0, "ê":0, "ë":0, "ę":0, "ě":0, "ĝ":0, "ğ":0, "ĥ":0, "î":0, "ì":0, "í":0, "ï":0, "ı":0, "ĵ":0, "ł":0, "ñ":0, "ń":0, "ň":0, "ò":0, "ö":0, "ô":0, "ó":0, "õ":0, "ø":0.76, "ř":0, "ŝ":0, "ş":0, "ś":0, "š":0, "ß":0, "ť":0, "þ":0, "ù":0, "ú":0, "û":0, "ŭ":0, "ü":0, "ů":0, "ý":0, "ź":0, "ż":0, "ž":0}
dictET = {"a":12.77, "b":0.82, "c":0, "d":4.41, "e":10.82, "f":0.14, "g":1.97, "h":1.81, "i":9.53, "j":1.79, "k":4.72, "l":6.23, "m":3.88, "n":5.35, "o":4.08, "p":1.64, "q":0, "r":2.76, "s":7.57, "t":7.51, "u":5.66, "v":2.33, "w":0, "x":0, "y":0, "z":0.04, "à":0, "â":0, "á":0, "å":0, "ä":1.36, "ã":0, "ą":0, "æ":0, "œ":0, "ç":0, "ĉ":0, "ć":0, "č":0, "ď":0, "ð":0, "è":0, "é":0, "ê":0, "ë":0, "ę":0, "ě":0, "ĝ":0, "ğ":0, "ĥ":0, "î":0, "ì":0, "í":0, "ï":0, "ı":0, "ĵ":0, "ł":0, "ñ":0, "ń":0, "ň":0, "ò":0, "ö":0.29, "ô":0, "ó":0, "õ":1.24, "ø":0, "ř":0, "ŝ":0, "ş":0, "ś":0, "š":0.02, "ß":0, "ť":0, "þ":0, "ù":0, "ú":0, "û":0, "ŭ":0, "ü":0.78, "ů":0, "ý":0, "ź":0, "ż":0, "ž":0.01}
dictGA = {"a":15.47, "b":2.48, "c":4.26, "d":3.75, "e":6.01, "f":1.59, "g":3.43, "h":7.87, "i":9.14, "j":0, "k":0, "l":3.9, "m":3.03, "n":7.36, "o":4.06, "p":0.67, "q":0, "r":5.95, "s":5.73, "t":4.77, "u":2.69, "v":0, "w":0, "x":0, "y":0, "z":0, "à":0, "â":0, "á":1.65, "å":0, "ä":0, "ã":0, "ą":0, "æ":0, "œ":0, "ç":0, "ĉ":0, "ć":0, "č":0, "ď":0, "ð":0, "è":0, "é":1.66, "ê":0, "ë":0, "ę":0, "ě":0, "ĝ":0, "ğ":0, "ĥ":0, "î":0, "ì":0, "í":1.84, "ï":0, "ı":0, "ĵ":0, "ł":0, "ñ":0, "ń":0, "ň":0, "ò":0, "ö":0, "ô":0, "ó":0.76, "õ":0, "ø":0, "ř":0, "ŝ":0, "ş":0, "ś":0, "š":0, "ß":0, "ť":0, "þ":0, "ù":0, "ú":0.83, "û":0, "ŭ":0, "ü":0, "ů":0, "ý":0, "ź":0, "ż":0, "ž":0}
dictGL = {"a":12.35, "b":1.27, "c":3.69, "d":4.31, "e":13.17, "f":1.09, "g":1.02, "h":1.01, "i":5.45, "j":0.14, "k":0.14, "l":3.23, "m":3.23, "n":6.93, "o":10.29, "p":3.16, "q":0.98, "r":7.02, "s":7.01, "t":5.07, "u":4.05, "v":1.24, "w":0.05, "x":0.68, "y":0.05, "z":0.47, "à":0, "â":0, "á":0.47, "å":0, "ä":0, "ã":0, "ą":0, "æ":0, "œ":0, "ç":0, "ĉ":0, "ć":0, "č":0, "ď":0, "ð":0, "è":0, "é":0.47, "ê":0, "ë":0, "ę":0, "ě":0, "ĝ":0, "ğ":0, "ĥ":0, "î":0, "ì":0, "í":0.54, "ï":0, "ı":0, "ĵ":0, "ł":0, "ñ":0.37, "ń":0, "ň":0, "ò":0, "ö":0, "ô":0, "ó":0.52, "õ":0, "ø":0, "ř":0, "ŝ":0, "ş":0, "ś":0, "š":0, "ß":0, "ť":0, "þ":0, "ù":0, "ú":0.29, "û":0, "ŭ":0, "ü":0.02, "ů":0, "ý":0, "ź":0, "ż":0, "ž":0}

freqEN = list(dictEN.values())
freqFR = list(dictFR.values())
freqDE = list(dictDE.values())
freqES = list(dictES.values())
freqPT = list(dictPT.values())
freqIT = list(dictIT.values())
freqTK = list(dictTK.values())
freqSW = list(dictSW.values())
freqPL = list(dictPL.values())
freqNL = list(dictNL.values())
freqDK = list(dictDK.values())
freqIS = list(dictIS.values())
freqFI = list(dictFI.values())
freqCZ = list(dictCZ.values())
freqNO = list(dictNO.values())
freqET = list(dictET.values())
freqGA = list(dictGA.values())
freqGL = list(dictGL.values())

freqList = [freqEN, freqFR, freqDE, freqES, freqPT, freqIT, freqTK, freqSW, freqPL, freqNL, freqDK, freqIS, freqFI, freqCZ, freqNO, freqET, freqGA, freqGL]
langDict = {"EN: ":0,"FR: ":0, "DE: ":0, "ES: ":0, "PT: ":0, "IT: ":0, "TK: ":0, "SW: ":0, "PL: ":0, "NL: ":0, "DK: ":0, "IS: ":0, "FI: ":0, "CZ: ":0, "NO: ":0, "ET: ":0, "GA: ":0, "GL: ":0}
langNames = list(langDict.keys())

def detectLang(s):
    freqText = []
    cosines = []
    #String preprocessing: removing punctuation, whitespace, and digits
    s = s.lower()
    s = ''.join([i for i in s if i not in string.punctuation and i not in string.whitespace and i not in string.digits])
    #Count every instance of a letter in the input string, then estimate frequency
    for instance in baseChars:
        inst = s.count(instance)
        freqText.append((inst*100)/len(s))
    #Calculate cosine similarity between input string's and each language's letter frequency 
    for elem in range(len(freqList)):
        langDict[langNames[elem]] = 1-spatial.distance.cosine(freqList[elem], freqText)

    newLangDict = sorted(langDict.values(), reverse = True)
    newLangNames = sorted(langDict, key=langDict.get, reverse = True)

    print("Cosine similarity (descending order):")
    for item in range(len(freqList)):
        print(newLangNames[item], newLangDict[item])
    print()
    time.sleep(5)
    #finalDict = dict(zip(newLangNames, newLangDict))
    #finalDict = str(finalDict)
    #return(finalDict)

def main():
    flag = True

    print("************")
    print("*DetectLang*")
    print("*(ver. 1.0)*")
    print("************")
    time.sleep(2)
    os.system('cls')
    print("Can detect the following languages: English (EN), French (FR), German (DE), Spanish (ES), Portuguese (PT), Italian (IT), Turkish (TK), Swedish (SW), Polish (PL), Dutch (NL), Danish (DK), Icelandic (IS), Finnish (FI), Czech (CZ), Norwegian (NO), Estonian (ET), Irish (GA), Galician (GL)")
    time.sleep(5)

    while flag:
        os.system('cls')
        print("*MENU*")
        print("Detect string's language [1]")
        print("Detect .txt file's language [2]")
        print("Exit [0]\n")
        try:
            ans = int(input(""))
            print()
            if(ans == 1):
                s = input("Enter string: ")
                print()
                if(len(s) <= 50):
                    print("[For more reliable results, the string should be longer]")
                    time.sleep(2)
                    print()
                print("Save detection to file? [Y][N]\n")
                save = input()
                save = save.upper()
                if(save == "Y"):
                    filename = input("File name?\n")
                    with open(filename, 'w') as file:
                        file.write(detectLang(s))
                        file.close()
                    print()
                else:
                    if(s == "0"):
                        flag = False
                    else:
                        detectLang(s)
            elif(ans == 2):
                filename = input("Enter the file's name: ")
                if(not os.path.exists(filename)):
                    print("File", filename, "does not exist in working directory!\n")
                    time.sleep(2)
                else:
                    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
                    with open(os.path.join(__location__, filename)) as file:
                        text = file.read()
                        print("Save detection to file? [Y][N]\n")
                        save = input()
                        save = save.upper()
                        if(save == "Y"):
                            filename = input("File name?\n")
                            file = open(filename, 'w')
                            file.write(detectLang(text))
                            file.close()
                            print()
                        else:
                            detectLang(text)
            else:
                flag = False
        except(SyntaxError, TypeError, ValueError, NameError, ZeroDivisionError):
            print("Invalid input! Try again...")
main()
