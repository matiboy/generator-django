import git
import migration
import notify
import pip
import sass
import server
import shell
import test

migrates = migration.Migrate()

tests = test.Test()

local_shell = shell.Shell()
pf = pip.PipFreeze()
pi = pip.PipInstall()

local_server = server.Server()
local_sass = sass.SassCompile()
