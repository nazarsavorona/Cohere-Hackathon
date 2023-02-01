def write_to_file(filename, output):
    f = open(f"../output/{filename}", "w")
    f.write(output)
    f.close()