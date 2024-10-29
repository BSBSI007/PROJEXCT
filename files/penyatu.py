import os

# Fungsi untuk menulis semua baris ke file hasil yang ditentukan oleh pengguna
def write_result_file(output_file):
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for filename in os.listdir('.'):
            if filename.endswith('.txt') and filename != output_file:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as file:  # Menambahkan errors='ignore'
                    for line in file:
                        result_file.write(line)

# Main
if __name__ == "__main__":
    # Meminta nama file output dari pengguna
    output_file = input("Masukkan nama file output (misalnya, 'result.txt'): ")

    # Memanggil fungsi untuk menulis hasil
    write_result_file(output_file)
    print(f"Semua baris telah disatukan ke dalam {output_file}")
