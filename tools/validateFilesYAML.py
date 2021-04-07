from __future__ import absolute_import, division, print_function
import os
import sys
import yaml

def searhFile(_starting_dir):
    base_dir = os.getcwd()+"/"+_starting_dir+"/"
    type_of_file=".yaml"
    yaml_dir = os.path.dirname(base_dir)
    success = False
    for file_name in os.listdir(yaml_dir):
        yaml_file = "{}/{}".format(yaml_dir,file_name)
        if os.path.isfile(yaml_file) and type_of_file in yaml_file:
            try:
                success,msg_ret = checkFile(yaml_file)
                print (msg_ret)
                if not success:
                    sys.exit(1)
            except Exception:
                print ("Error calling function {}".format("yamlcheckFile(_fileToCheck)_file)"))
                sys.exit(1)
    return success

def checkFile(_fileToCheck):
    print(" > File a verificar --> {}".format(_fileToCheck))
    try:
        with open(_fileToCheck) as file:
            file_yaml = file.read()
        parsedYml = yaml.load(file_yaml, Loader=yaml.FullLoader)
        success = True
        msg_ret= " > Sintaxis correcta, file: {} ".format(_fileToCheck)
    except FileNotFoundError as error:
        success = False
        msg_ret = " > {} File Error {}".format(error, "\n")
    except Exception as error:
        success = False
        msg_ret= " > {} error formato yaml {}".format(error, "\n")
    return success, msg_ret

if __name__ == "__main__":
    if len(sys.argv) == 2:
        dir_raiz_str = str(sys.argv[1])
        dir_raiz = dir_raiz_str.split(",")
        for dir in dir_raiz:
            dir = dir.replace("/","")
            print(" >", "*" * 120)
            print(" > NEP@L dice: checking .yaml files structure in {}".format(dir))
            searhFile(dir)
            print(" >", "*" * 120)
    elif len(sys.argv) > 2:
        print(" > {} Error: Cantidad no válida de argumentos, ingrese solo <directorio raiz> a chequear {}".format("\n", "\n"))
    else:
        print (" > Python dice: checking .yaml files structure {} in {} directorio raiz".format("\n", dir_raiz))
