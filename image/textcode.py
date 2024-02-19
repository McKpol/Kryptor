from PIL import Image, ImageDraw, ImageFont

# Zmienna zawierająca litery
letters = 'QWERTYUIOPASDFGHJKLZXCVBNM{}:">?[];\'./!@#$%^&*()_+1234567890-=\\|'

# Wymiary obrazu
image_width = 100
image_height = 100

# Stworzenie obrazu dla każdej litery
for letter in letters:
    # Stworzenie pustego obrazu
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Ustawienie czcionki
    font = ImageFont.load_default()

    # Wymiary tekstu
    text_width, text_height = draw.textsize(letter, font=font)

    # Pozycja, aby wyśrodkować tekst
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    # Narysowanie tekstu na obrazie
    draw.text((x, y), letter, fill="black", font=font)

    # Zapisanie obrazu do pliku
    image.save(f"letter_{ord(letter)}.png")  # Zapisuje każdą literę z kodem Unicode
