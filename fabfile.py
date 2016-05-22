from fabric.api import cd,run,env,hosts,roles,execute,settings,local
import os



env.hosts = 'grad'
env.user="root"

def save():
	local("git add -A")
	with settings(warn_only=True):
		local("git commit -m 'save' ")
		local("git push")

def dep():
	with cd("cd /data/src"):
		run ("git pull")
		# local("git checkout master")
		# local("git merge ProfessorPaul")
