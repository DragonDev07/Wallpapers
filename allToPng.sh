#!/bin/zsh

echo "Converting .jpg files to .png..."

for jpg_file in **/*.jpg; do
    if [ -f "$jpg_file" ]; then
        png_file="${jpg_file%.jpg}.png"
        echo "Converting $jpg_file to $png_file"
        convert "$jpg_file" -quality 100 "$png_file"
        rm "$jpg_file"
    fi
done

echo "Conversion complete."
