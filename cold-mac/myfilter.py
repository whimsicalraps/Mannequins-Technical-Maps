from panflute import *

def create_header_pagebreak(elem, doc):
	if type(elem) == Header:
		if elem.level < 3:
			return [RawBlock('\\cleardoublepage','tex'),elem]
	if isinstance(elem,Div):
		return RawBlock('\\cleardoublepage','tex')

def main(doc = None):
    return run_filter(create_header_pagebreak, doc = doc)

if __name__ == '__main__':
    main()