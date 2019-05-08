def duplicate_count(text):
  firstSeen = []
  duplicates = []
  characters = list(text.lower())
  for character in characters:
    if character in firstSeen and character in duplicates:
      True
    elif character in firstSeen and character not in duplicates:
      duplicates.append(character)
    elif character not in firstSeen:
      firstSeen.append(character)
    else:
      print("whoops")
  return len(duplicates)
