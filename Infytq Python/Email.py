s="amit@sccilabs.com"

start=s.index('@')
end=len(s)-s[::-1].index('.')

print(s[start+1:end-1])
