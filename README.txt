ExSvn - extended subversion tools
=================================

This project is intended to automate some of the common tasks, related to
source control, author is routinely performing at his workplace. This project
implements set of tools to make those task less boring / time consuming / error
prone.

These tools are not intended for broad audience, since scope is rather specific
to author environment. However, one may find the codebase flexible enough to
tweak it for his own needs.

Project scope and goals 
=======================

Here are list of problems this project is aimed to solve:

  1. Never-commit files.
  
     In a project with several developers with different development
     environments developer's local working copy is often pollutes with changed
     files that should never be commited to the repository. There is no way to
     exclude such changed files from commit in a persistent fashion. Developer
     has to manually exclude such file when he commits each time. This is error
     prone situation.

     This project will implement its own `commit' function and own per-project
     configuration file, that will allow to specify set of files, that should
     never be commited. Proprietary `status' function will also be implemented
     that will hide never-commit files.

     Commit user interface will be based on standard text editor, much like the
     default subversion commit message prompt (that lists of changed files that
     are going to be commited), however list will be much more functional and
     will allow to select commitable files right in editor window. Author finds
     such mode of operation rather convinient and furthermore it is easier to
     implement than full GUI.

  2. Easier selection of files to commit.

     Sometimes not all changed files has to be commited. Commit interface will
     allow user toeasily check files intended for commit simply by editing
     pre-created text file.  The same editor is used for commit message
     composing. 

  3. List of assigned JIRA tickets to pick from

     Author' workplace policy states that all commit messages should include
     JIRA (issue control system) ticket numbers.  Commit interface will list
     all assigned jira tickets. User then will be able to just copy and paste
     related ticket numbers into commit message area.

