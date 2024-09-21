# SQL Parser

## About
This project is a sql parser.

It uses a recursive decent strategy with a hand written tokenizer and parser. I did this because I want to be able to have good error messages.

## Progress

### SQL Parser
- [x] select
- [x] delete
- [ ] create
- [ ] insert
- [ ] update
- [x] drop

### SQL Evaluator
- [ ] select
- [ ] delete
- [ ] create
- [ ] insert
- [ ] update
- [ ] drop

## Building
To build the project open the visual studio solution file and click build. You can also run `MSBuild.exe` in the src folder or `MSBuild.exe src` from the project directory.

## Testing
To test the project run pytest in the root directory or test folder. The code will try to build before the tests run so it is always the latest build. Most or all tests will fail if the build fails.

## Warning
Ensure your path contains `MSBuild.exe` as it is needed for building the project.