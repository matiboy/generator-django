import git
import migration
import pip
import sass
import server
import shell
import test
import curl

migrates = migration.Migrate()

tests = test.Test()

local_shell = shell.Shell()
pf = pip.PipFreeze()
pi = pip.PipInstall()

local_server = server.Server()
local_sass = sass.SassCompile()
