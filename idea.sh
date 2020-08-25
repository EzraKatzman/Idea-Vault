#!/bin/bash

function idea() {
    cd
    printf "What's your idea? "
    read;
    python '/c/Users/Ezkat/desktop/side projects/ideavault/posterboard.py' ${REPLY}
    printf "Would you like to make a Github repository for it? [Y/n]: "
    read answer
    case $answer in
        [yY]) 
            printf "Name the directory: "
            read dirname
            python '/c/Users/Ezkat/desktop/side projects/ideavault/initializer.py' $dirname
            ;;
        *)
            exit 
            ;;
    esac
}
idea
