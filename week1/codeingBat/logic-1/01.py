def cigar_party(cigars, is_weekend):
    if is_weekend:
      return cigars >= 40
    else:
      return 60 >= cigars >= 40