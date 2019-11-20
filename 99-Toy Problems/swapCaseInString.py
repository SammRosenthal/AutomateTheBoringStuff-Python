def swap_case(s):
   answer = ''
   for c in s:
      if c.isupper():
         answer += c.lower()
      else:
         answer += c.upper()
   return answer