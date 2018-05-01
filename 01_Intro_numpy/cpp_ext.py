def cpp(line, cell):
    """Compile, execute C++ code, and return the
    standard output."""
    # We first retrieve the current IPython interpreter instance.
    ip = get_ipython()
    # We define the source and executable filenames.
    source_filename = '_temp.cpp'
    program_filename = '_temp'
    # We write the code to the C++ file.
    with open(source_filename, 'w') as f:
        f.write(cell)
    # We compile the C++ code into an executable.
    compile = ip.getoutput("g++ {0:s} -o {1:s}".format(
              source_filename, program_filename))
    # We execute the executable and return the output.
    output = ip.getoutput('./{0:s}'.format(program_filename))
    print('\n'.join(output))

def load_ipython_extension(ipython):
       """This function is called when the extension is loaded.
       It accepts an IPython InteractiveShell instance.
       We can register the magic with the `register_magic_function`
       method of the shell instance."""
       ipython.register_magic_function(cpp, 'cell')