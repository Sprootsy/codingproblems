package main

import "testing"

func Test_deleteAndEarn(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Test [3,4,2]",
			args: args{nums: []int{3,4,2}},
			want: 6,
		},
		{
			name: "Test [2,2,3,3,3,4]",
			args: args{nums: []int{2,2,3,3,3,4}},
			want: 9,
		},
		{
			name: "Test [2,2,3,3,3,4]",
			args: args{nums: []int{1,8,5,9,6,9,4,1,7,3,3,6,3,3,8,2,6,3,2,2,1,
				2,9,8,7,1,1,10,6,7,3,9,6,10,5,4,10,1,6,7,4,7,4,1,9,5,1,5,7,5}},
			want: 138,
		},
		{
			name: "Test [3,1]",
			args: args{nums: []int{3,1}},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := deleteAndEarn(tt.args.nums); got != tt.want {
				t.Errorf("deleteAndEarn() = %v, want %v", got, tt.want)
			}
		})
	}
}
