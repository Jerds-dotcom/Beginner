def slicer(id_):
	username = id_[:id_.index('@')] # slices the username
	domain = id_[id_.index('@') + 1:] # slices the domain 
	return username, domain