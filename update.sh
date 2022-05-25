#!/bin/bash

#Made by: Alexander Epstein https://github.com/alexanderepstein

currentVersion="0.1.0" 
repositoryName="GoogleAutoLogin"
githubUserName="N1sek" 
nameOfInstallFile="install.sh" 


## This function determines which http get tool the system has installed and returns an error if there isnt one
getConfiguredClient()
{
  if  command -v curl &>/dev/null; then
    configuredClient="curl"
  elif command -v wget &>/dev/null; then
    configuredClient="wget"
  elif command -v http &>/dev/null; then
    configuredClient="httpie"
  elif command -v fetch &>/dev/null; then
    configuredClient="fetch"
  else
    echo "Error: This tool reqires either curl, wget, httpie or fetch to be installed\." >&2
    return 1
  fi
}

## Allows to call the users configured client without if statements everywhere
httpGet()
{
  case "$configuredClient" in
    curl)  curl -A curl -s "$@" ;;
    wget)  wget -qO- "$@" ;;
    httpie) http -b GET "$@" ;;
    fetch) fetch -q "$@" ;;
  esac
}

update()
{
if [[ $currentVersion == "" || $repositoryName == "" || $githubUserName == "" || $nameOfInstallFile == ""  || $latestVersion == "" ]];then
  echo "Error: update utility has not been configured correctly." >&2
  return 1
else
  if [[ "$latestVersion" != "$currentVersion" ]]; then
    echo "Version $latestVersion available"
    echo -n "Do you wish to update $repositoryName [Y/n]: "
    read -r answer
    if [[ "$answer" == "Y" || "$answer" == "y" ]] ;then
      cd  ~ || { echo 'Update Failed' ; return 1 ; }
      if [[ -d  ~/$repositoryName ]]; then rm -r -f $repositoryName  || { echo "Error: permissions denied deleting old clone, try running thr update as sudo" ; return 1 ; }; fi
      git clone "https://github.com/$githubUserName/$repositoryName" || { echo "Couldn't download latest version" ; return 1; }
      cd $repositoryName ||  { echo 'Update Failed' ; return 1 ;}
      git checkout "v$latestVersion" 2> /dev/null || git checkout "$latestVersion" 2> /dev/null || echo "Couldn't git checkout to stable release, updating to latest commit."
      #chmod a+x install.sh #this might be necessary in your case but wasnt in mine.
      "./$nameOfInstallFile" || return 1 # could echo error here about sudo but I assume you handle errors in your own script correctly
      cd ..
      rm -r -f $repositoryName || { echo "Error: successfully updated but couldn't delete temperary files at ~/$repositoryName"; return 1; }
    else
      return 1
    fi
  else
    echo "$repositoryName is already the latest version"
  fi
fi
}

checkInternet()
{
  httpGet google.com > /dev/null 2>&1 || { echo "Error: no active internet connection" >&2; return 1; } # query google with a get request
}


getConfiguredClient || exit 1
checkInternet || exit 1
latestVersion=$(httpGet https://api.github.com/repos/$githubUserName/$repositoryName/tags | grep -Eo '"name":.*?[^\\]",'| head -1 | grep -Eo "[0-9.]+" ) #always grabs the tag without the v option
update || exit 1
