list_1 = [('Dhruvi Acharya', '1975'), ('Joseph Aaron', '1959'), ('Hans Aarsman', '1951'), ('Michael Abrams', '1957'),
          ('Scoli Acosta', '1973'), ('Abdullah  M. I. Syed', '1974'), ('Fiona Ackerman', '1978'),
          ('Francis Acea', '1967'), ('Hamra Abbas', '1976'), ('Matthew Abbott', '1965'), ('Samira Abbassy', '1965'),
          ('Roger Ackling', '1947'), ('Aoussef Abdelke', '1966'), ('Bigo 23', '1966'), ('Norman Ackroyd', '1938')]


list_1.sort(key=lambda x: x[0])
print(list_1)
output = sorted(list_1, key=lambda x: x[1])
print(output)
