def emojiConverter(message):
    words=message.split()
    emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😃"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

print(emojiConverter("Hey honey :) !"))