

pipeline{
    agent {node {label "local-agent-01"}}

    environment{
        String getCode = "Start to get automation test scripts from github.."
        String buildimage = "Start to build docker image.."
        String runTestScripts = "Start to run test scripts.."
        String getTestResult = "Get test result.."

    }

    options{
        timestamps() //在每一行的log中都加上时间
        skipDefaultCheckout() //跳过一开始就会去拉仓库的最新代码
        disableConcurrentBuilds() //禁用并行
        timeout(time: 1, unit: 'HOURS')
    }

	stages{
		//清理数据
		stage("Clear data"){
		    steps {
		        bat '''
		            del /f /s /q test_report.html
		            rmdir /s /q .pytest_cache
		        '''
		        }
	    }


	    // 拉取最新的测试脚本
	    stage("Get code from github"){
	        steps{
	            timeout(time: 3, unit: 'MINUTES') {
	                script {
	                    println(env.getCode)
	                    retry(count:10,sleep:20){
	                        checkout scm
	                    }

	                }

	            }
	        }
	    }


		// 安装相关的依赖
		stage("install packages"){
			steps{
				bat '''
	                E:\\SoftWareInstalled\\python\\python.exe -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple
	                E:\\SoftWareInstalled\\python\\python.exe -m pip install -r requirements.txt --timeout 120 --retries 5 -i https://mirrors.aliyun.com/pypi/simple
	            '''
			}
		}


	    // 运行脚本
	    stage("run test scripts"){
	        steps{
	            timeout(time:5, unit:"MINUTES")
	            script{
	                println(env.runTestScripts)
	                bat "E:\\SoftWareInstalled\\python\\python.exe run_test.py"
	            }

	        }
	    }

	}
	//后置处理
	post{

		// 一定会处理的
		always{
			publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'test_report.html',
                reportName: '自动化测试报告'])
            }


		// 构建成功的处理
		success{
			script{
				println("Success")
				currentBuild.description += "\n 构建成功"
			}
		}

		//构建失败的处理
		failure{
			script{
				println("failure")
                currentBuild.description += "\n 构建失败"
			}
		}

		//构建取消的处理
		aborted{
			script{
				println("aborted")
				currentBuild.description += "/n 构建取消"
			}


		}

	}


}