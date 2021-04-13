from invoke import task

@task
def start(ctx):
  ctx.run("python3 src/user_interface.py")

@task
def test(ctx):
  ctx.run("pytest src")

@task 
def coverage(ctx):
  ctx.run("coverage run --branch -m pytest src")

@task
def coverage_report(coverage):
  ctx.run("coverage report -m")