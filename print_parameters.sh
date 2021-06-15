#This script will print all the parameter store parameters of the default region

parameter_names=();
aws ssm describe-parameters \
| jq '.Parameters' \
| jq '.[].Name' \
| while IFS= read -r line
do
	param_name="${line:1}"
	param_name=${param_name%?}
	parameter_names[${#parameter_names[@]}]=$param_name
	aws ssm get-parameters --names $param_name --with-decryption | jq '.Parameters[] | "\(.Name)-> \(.Value)"'
done