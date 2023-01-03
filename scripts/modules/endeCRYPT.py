# This script encodes and decodes pswd file


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '^', '{','}', '[', ']',
         '!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_', '=', '`',
         '~', '<', '>', '?', '.', ',', '\n', ' ', '\t', ':', ';', "'", '"']


specialChars = [')=#\n', '_58\n', 'eR9\n', '93c\n', 'Kf~\n', '66C\n', '49)\n', '$6%\n',
                '0-2\n', '`%7\n', 'n9K\n', 'Y89\n', '%9_\n', '!H?\n', '&HZ\n', 't82\n',
                '#X1\n', ',)6\n', '0?,\n', 'g4*\n', '`Q!\n', '1iQ\n', 'f4F\n', 'V76\n',
                '((7\n', '-~9\n', '4Si\n', '9l~\n', '1K1\n', '377\n', '&pA\n', 'ahR\n',
                '9n3\n', 'Z?7\n', 'Uy9\n', 'v$z\n', 'in3\n', '4K*\n', 'M7`\n', 'P02\n',
                '7)j\n', '4`=\n', '~&g\n', '<`!\n', 'g%2\n', '%3?\n', '37P\n', 'D7(\n',
                'hxk\n', '_`0\n', '51$\n', 'g0)\n', '~v+\n', '4ho\n', '6yF\n', '7(O\n',
                '0j8\n', ')>4\n', '*t6\n', '_x<\n', 'x93\n', 'U20\n', 'nCN\n', '*4n\n',
                'K7g\n', '$.6\n', '3%q\n', '55`\n', 'SgT\n', 'Dk3\n', '=R~\n', '0U.\n',
                '1(F\n', '!=4\n', 'h7&\n', '%9>\n', 'Y7A\n', '3s8\n', 'pdh\n', '#Z+\n',
                'I84\n', '9q$\n', 'AU(\n', 'b%q\n', 's&2\n', 'a*1\n', '10#\n', 'g8*\n',
                'D&1\n', 'h^2\n', 'S7=\n', 'v^6\n', 'z0&\n', '45!\n']


def encode_file(filePath):

    new_file = ""
    shift = 13
    file = open(filePath, 'r').readlines()

    for words in file:
        for i in range(len(words)):
            index = chars.index(words[i])
            new_index = (index + shift) % len(specialChars)
            new_file += specialChars[new_index]

    with open(filePath, 'w') as file:
        file.writelines(new_file)


def decode_file(filePath):

    new_file = ""
    shift = 13
    with open(filePath, 'r') as file:

        for words in file:

            index = specialChars.index(words)
            new_index = index - shift
            if new_index < 0:
                new_index = len(chars) + new_index
            new_file += chars[new_index]

    with open(filePath, 'w') as file:
        file.writelines(new_file)
