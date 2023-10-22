import aspose.pdf as ap

peso = 138
altura = 190
idade = 26

tmb = 10 * peso + 6.25 * altura - 5 * idade + 5

# Inicializar objeto de documento
document = ap.Document()

# Adicionar Página
page = document.pages.add()
page2 = document.pages.add()

# Inicializar objeto textfragment
text_fragment = ap.text.TextFragment("Hello,world!")
nome = ap.text.TextFragment("Thyago Holanda Monteiro de Lima")
taxa_metabolica = ap.text.TextFragment(f"Sua taxa metabolica basal é {tmb}")

# Adicionar fragmento de texto à nova página
page.paragraphs.add(text_fragment)
page2.paragraphs.add(nome)
page2.paragraphs.add(taxa_metabolica)

# Salvar PDF atualizado
document.save("output.pdf")
