#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

text = """abobaa abob aaaaab booooob acb alolololadablkaskb aobabb BOB ABOB."""

print (re.findall("a+[a-z]+b+", text))
