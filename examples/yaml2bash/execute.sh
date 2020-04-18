#!/bin/sh
yaml_path=config.yaml
global_env_keyword="global_env"
local_env_keyword="local_env"

# YAML Parsing does not support list. Accessing values of list may cause incorrect
parse_yaml() {
   local prefix=$2
   local s='[[:space:]]*' w='[a-zA-Z0-9_]*' fs=$(echo @|tr @ '\034')
   sed -ne "s|^\($s\):|\1|" \
        -e "s|^\($s\)\($w\)$s:$s\([\"'].*[\"']\)$s\$|\1$fs\2$fs\3|p" \
        -e "s|^\($s\)\($w\)$s:$s\(.*\)$s\$|\1$fs\2$fs\3|p"  $1 |
   awk -v ignore_keys="$global_env_keyword,$local_env_keyword" -F$fs '{
      ignore_length = split(ignore_keys, ignore_list, ",")
      indent = length($1)/2;
      vname[indent] = $2;
      for (i in vname) {if (i > indent) {delete vname[i]}}
      if (length($3) > 0) {
         vn=""; 
         for (i=0; i<indent; i++) {
            ignore=0
            is_global=0
            for (j=1; j<ignore_length+1; j++){
               if(vname[i] == ignore_list[j]){
                  ignore=1
               }
            }
            is_global=vname[i]==ignore_list[1]
            if (is_global) {
               vn="export "
            }
            else if (!ignore) {
               vn=(vn)(vname[i])("__")
            }
         }
         printf("%s%s%s=%s\n", "'$prefix'",vn, $2, $3);
      }
   }'
}

# Load all variable in scope "bash" of YAML config
init_variable(){
   echo ">> Config from $yaml_path "
   yaml2bash --yaml $yaml_path
   echo '>> Assign variable automatically...'
   yaml2bash --yaml $yaml_path | parse_yaml ""
   eval $(yaml2bash --yaml $yaml_path | parse_yaml "")

}

init_variable
echo Name from config: $name
