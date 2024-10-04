#!/bin/bash
if [ -z "$1" ]
then
    echo "No environment argument supplied, defaulting to dev"
    cp app/dev.env app/.env
else
    case $1 in
        dev|prod)
            cp app/$1.env app/.env
            ;;
        *)
            echo "Invalid environment. Use dev or prod."
            exit 1
            ;;
    esac
fi

set -a; source app/.env; set +a

while IFS= read -r line
do
    if [[ $line == *=* && $line != "#"* ]]; then
        name=$(echo $line | cut -d'=' -f1)
        echo $name=${!name}
    fi
done < app/.env

if [ -z "$1" ] || [ $1 != "prod" ]
then
    fastapi dev app/main.py
else
    fastapi run app/main.py
fi
