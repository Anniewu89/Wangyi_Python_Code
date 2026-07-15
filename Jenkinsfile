

pipeline{
    agent {node {label "local-anget-01"}}

    env{
        String getCode = "Start to get automation test scripts from github.."
        String buildimage = "Start to build docker image.."
        String runTestScripts = "Start to run test scriptis.."
        String getTestResult = "Get test result.."

    }

    options{
        timestamps() //在每一行的log中都加上时间
        skipDefaultCheckout() //跳过一开始就会去拉仓库的最新代码
        disableConcurrentBuilds() //禁用并行
        timeout(time: 1, unit: 'HOURS')
    }


    // 拉取最新的测试脚本
    stage{
        steps{
            timeout(time: 3, unit: 'MINUTES') {
                script {
                    println(${evn.getCode})}
                    checkout scm
                }


            }
        }
    }


    // 运行脚本
    stage{
        steps{
            timeout(time:5, unit:"MINUTES")
            script{
                println(${env.runTestScripts})
                sh "python run_test.py"
            }

        }
    }


	//后置处理
	post{

		// 一定会处理的
		always{
			script{
				println(${env.getTestResult})
			}
		}

		// 构建成功的处理
		success{
			script{
				println("Success")
				currentBuild.description += "\n 构建成功"
			}
		}

		//构建失败的处理
		failure {
			script{
				println("failure")
                currentBuild.description += "\n 构建失败"
			}
		}

		//构建取消的处理
		aborted {
			script{
				println("aborted")
				currentBuild.description =+ "/n 构建取消"
			}


		}

	}



}