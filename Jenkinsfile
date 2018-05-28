node()
{

   checkout scm

   sh "rm -f *.deb"
   sh "git checkout master"
   sh "git pull"
   sh "make deb"
   sh "mv ../*.deb ."
}
