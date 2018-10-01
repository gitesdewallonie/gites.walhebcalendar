node()
{
  stage 'checkout'
  deleteDir()
  checkout scm
  stage 'build'
  sh "make deb"
  stage 'publish'
  sh "make publish-deb"
}
