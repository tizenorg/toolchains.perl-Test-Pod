#!perl -T

use strict;

use Test::Builder::Tester tests => 2;
use Test::More;

BEGIN {
    use_ok( 'Test::Pod' );
}

my $file = 't/item-ordering.pod';
test_out( "not ok 1 - POD test for $file" );
pod_file_ok( $file );
test_fail(-1);
test_diag(
    "$file (32): You can't have =items (as at line 36) unless the first thing after the =over is an =item",
);
test_test( "$file is bad" );
