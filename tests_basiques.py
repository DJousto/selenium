import pytest

def test_1():
	assert (1, 2, 3) == (1, 2, 3)

def test_2():
	assert 1 > 2
	assert 3 > 2
	assert "a" in "abc"
	

def test_web1():
	assert 3 > 2
	assert "a" in "abc"
	assert 1 > 2
	

def test_web2():
	assert 1 > 2
	assert 3 > 2
	assert "a" in "abc"
	

