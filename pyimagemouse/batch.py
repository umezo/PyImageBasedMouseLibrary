# -*- coding: utf-8 -*-

import core
import time

SCREEN_CAPTURE_PATH = None

############################################################################
# スクリーンキャプチャからテンプレート画像の座標を返す
# @param templatePath {String} テンプレート画像
# @param skip=False {Boolean} テンプレート画像が見つからなかった時に例外にするかどうか. Trueだと例外は投げられない
# @return {Tuple} or False テンプレートの中心座標。パラメータskipがTrueでテンプレートが見つからなかったときFalse
def getPoint(templatePath,skip=False):
  captureScreen()
  point = core.detect( templatePath , SCREEN_CAPTURE_PATH )

  if not point:
    if skip:
      return False
    else:
      raise ValueError( templatePath )

  return point

# スクリーンキャプチャからテンプレート画像の位置をクリックします
# @param templatePath {String} テンプレート画像
# @param skip=False {Boolean} テンプレート画像が見つからなかった時に例外にするかどうか. Trueだと例外は投げられない
# @return {Boolean} クリックをスキップしたかどうか. skipしてればTrue = clickしたらFalse
def click( templatePath ,skip=False):
  point = getPoint( templatePath, skip )

  if not point:
    return True

  core.click( point )

  #マウスの位置がそのままだと、画面が変化しマウスオーバーが発生したりするので逃がす
  core.move( (5,5) )

  #気休め
  #これを入れとくと精度が上がる気がする
  time.sleep( 0.2 )
  return False

# スクリーンキャプチャからテンプレート画像の位置にマウスを移動する
# @param templatePath {String} テンプレート画像
# @param skip=False {Boolean} テンプレート画像が見つからなかった時に例外にするかどうか. Trueだと例外は投げられない
# @return {Boolean} 移動をスキップしたかどうか. skipしてればTrue = moveしたらFalse
def move( templatePath ,skip=False):
  point = getPoint( templatePath, skip )

  if not point:
    return True 

  core.move( point )
  return False

# templatePathで指定された画像がスクリーンキャプチャに存在するかどうか返す
# @param templatePath {String} テンプレート画像
# @return {Boolean} テンプレートが存在したかどうか
def detect(templatePath):
  point = getPoint( templatePath , True )

  if not point:
    return False
  else:
    return True

# 画面をキャプチャする
def captureScreen():
  core.capture( SCREEN_CAPTURE_PATH )

