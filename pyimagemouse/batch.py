# -*- coding: utf-8 -*-

import core
import time

import tempfile

SCREEN_CAPTURE_PATH = tempfile.gettempdir() + '/screenshot.png'

############################################################################
def getPoint(templatePath,skip=False):
  """
  通常、パッケージ外からこの関数を直接コールすることはない
  スクリーンキャプチャからテンプレート画像の座標を返す
  @param templatePath {String} テンプレート画像
  @param skip=False {Boolean} テンプレート画像が見つからなかった時に例外にするかどうか. Trueだと例外は投げられない
  @return {Tuple} or False テンプレートの中心座標。パラメータskipがTrueでテンプレートが見つからなかったときFalse
  """
  captureScreen()
  point = core.detect( templatePath , SCREEN_CAPTURE_PATH )

  if not point:
    if skip:
      return False
    else:
      raise ValueError( templatePath+' did not found in screen')

  return point

def click( templatePath ,skip=False):
  """
  スクリーンキャプチャからテンプレート画像の位置をクリックします
  @param templatePath {String} テンプレート画像。クリックする対象の画像
  @param skip=False {Boolean} テンプレート画像が見つからなかった時に例外にするかどうか. Trueだと例外は投げられない
  @return {Boolean} クリックをスキップしたかどうか. skipしてればTrue = clickしたらFalse
  """
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

def move( templatePath ,skip=False):
  """
  スクリーンキャプチャからテンプレート画像の位置にマウスを移動する
  @param templatePath {String} テンプレート画像。クリックする対象の画像
  @param skip=False {Boolean} テンプレート画像が見つからなかった時に例外にするかどうか. Trueだと例外は投げられない
  @return {Boolean} 移動をスキップしたかどうか. skipしてればTrue = moveしたらFalse
  """
  point = getPoint( templatePath, skip )

  if not point:
    return True 

  core.move( point )
  return False

def detect(templatePath):
  """
  templatePathで指定された画像がスクリーンキャプチャに存在するかどうか返す
  @param templatePath {String} テンプレート画像
  @return {Boolean} テンプレートが存在したかどうか
  """
  point = getPoint( templatePath , True )

  if not point:
    return False
  else:
    return True

def captureScreen():
  """
  通常、パッケージ外からこの関数を直接コールすることはない
  画面をキャプチャする
  """
  core.capture( SCREEN_CAPTURE_PATH )

