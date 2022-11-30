library('qrcode')

code <- qr_code("https://gradhub2022.github.io/")
generate_svg(code, filename = "gradhub2022code.svg")