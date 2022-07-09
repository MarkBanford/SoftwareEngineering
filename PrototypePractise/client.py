from document import Document

ORIGINAL_DOC = Document("Original", [[1, 2, 3, 4], [5, 6, 7, 8]])
print(ORIGINAL_DOC)

DOC_COPY_1 = ORIGINAL_DOC.clone(3)
DOC_COPY_1.name = "Copy1"
DOC_COPY_1.list[1][2] = 200
print(DOC_COPY_1)
print(ORIGINAL_DOC)
