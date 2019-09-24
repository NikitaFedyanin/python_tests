"""
Своеобразная система контроля версий для текстового редактора
"""


class TextEditor:
    text = ''
    style = None

    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.style = '[{}]'.format(font)

    def show(self):
        if self.style:
            return '{0}{1}{0}'.format(self.style, self.text)
        return self.text

    def restore(self, version):
        self.text = version[0]
        self.style = version[1]


class SavedText:
    versions = {0: ['', None], 1: ['', None], 2: ['', None], 3: ['', None], 4: ['', None],
                 5: ['', None], 6: ['', None], 7: ['', None], 8: ['', None], 9: ['', None]}
    text_editor = TextEditor()
    state = -1

    def save_text(self, current_text):
        self.state += 1
        self.versions[self.state] = [current_text.text, current_text.style]

    def get_version(self, ver_number):
        return self.versions[ver_number]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = TextEditor()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
