import fitz
class ToolKit:
    def __init__(self) -> None:
        pass

    @staticmethod
    def read_file(file: str) -> str:
        with open(file, "r") as f:
            return f.read()

    @staticmethod
    def pdf_to_text(pdf_file):
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
        return text

    def create_prompt(self, filename: str) -> str:
        try:
            prompt = self.read_file(filename)
        except:
            with open(filename, 'r', encoding='utf-8') as file:
                prompt = file.read()

        template = f"""
            {prompt}
            """
        return template